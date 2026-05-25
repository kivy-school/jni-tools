import Foundation
import PySwiftAST
import PySwiftCodeGen

/// Orchestrates: `[input dir] -> JAR -> JSON -> AstDocument -> Python files`.
public struct Pipeline {

    /// Which extraction backend to use.
    public enum Backend: String, Sendable {
        /// Legacy: launch `java -jar java-ast-emitter.jar` subprocess and parse JSON.
        case java
        /// New: use swift-java embedded JVM to reflect on classes in-process.
        case swiftJava = "swift-java"
    }

    public struct Options {
        public var inputDir: URL
        public var outputDir: URL
        public var jarPath: URL
        public var javaExecutable: String
        public var fileLayout: FileLayout
        /// Which extraction backend to use. Defaults to `.java` for backward compat.
        public var backend: Backend
        /// When true, strip the longest common reverse-DNS prefix shared by
        /// every emitted class (e.g. `com.google.android.gms.`) so the
        /// output tree is short and Pythonic instead of mirroring Java's
        /// package convention.
        public var stripCommonPackagePrefix: Bool
        /// Maps a Java package prefix (must end with `.`) to an existing
        /// Python module prefix. Used by the `.pyi` emitter to route
        /// unwrapped externals into a pre-existing wrapper package
        /// instead of synthesizing forward-declared stubs.
        public var externalModules: [(javaPrefix: String, pyPrefix: String)]

        public init(inputDir: URL, outputDir: URL, jarPath: URL,
                    javaExecutable: String = "java",
                    fileLayout: FileLayout = .perClass,
                    backend: Backend = .java,
                    stripCommonPackagePrefix: Bool = true,
                    externalModules: [(javaPrefix: String, pyPrefix: String)] = []) {
            self.inputDir = inputDir
            self.outputDir = outputDir
            self.jarPath = jarPath
            self.javaExecutable = javaExecutable
            self.fileLayout = fileLayout
            self.backend = backend
            self.stripCommonPackagePrefix = stripCommonPackagePrefix
            self.externalModules = externalModules
        }
    }

    /// Output layout strategy.
    public enum FileLayout {
        /// One `.py` file per class, mirroring the Java package hierarchy.
        case perClass
        /// All classes flattened into a single file (debug helper).
        case singleFile
    }

    public enum PipelineError: Error, CustomStringConvertible {
        case javaFailed(exitCode: Int32, stderr: String)
        case decodeFailed(String)
        case swiftJavaBackendNotLinked

        public var description: String {
            switch self {
            case .javaFailed(let code, let err):
                return "java-ast-emitter exited \(code): \(err)"
            case .decodeFailed(let msg):
                return "AST JSON decode failed: \(msg)"
            case .swiftJavaBackendNotLinked:
                return "swift-java backend requested but SwiftJavaReflector module is not linked. Use Pipeline.runWithReflector() from the CLI target."
            }
        }
    }

    public init() {}

    public func run(_ opts: Options) throws -> [URL] {
        let doc: AstDocument
        switch opts.backend {
        case .java:
            let json = try invokeJar(opts: opts)
            do {
                doc = try JSONDecoder().decode(AstDocument.self, from: json)
            } catch {
                throw PipelineError.decodeFailed(String(describing: error))
            }
        case .swiftJava:
            // Defer to the SwiftJavaReflector module (loaded dynamically to avoid
            // hard-linking swift-java into every target). The caller must ensure
            // SwiftJavaReflector is linked and call `Pipeline.runWithReflector(_:doc:)`
            // or pass a pre-built AstDocument via `emit(doc:opts:)`.
            throw PipelineError.swiftJavaBackendNotLinked
        }
        return try emit(doc: doc, opts: opts)
    }

    /// Decoupled hook so tests can feed a pre-baked AST without launching the JVM.
    public func emit(doc: AstDocument, opts: Options) throws -> [URL] {
        let emitter = PyWrapperEmitter()
        let pyiEmitter = PyiStubEmitter()
        try FileManager.default.createDirectory(at: opts.outputDir,
                                                withIntermediateDirectories: true)
        var written: [URL] = []

        // Compute prefix to strip (or empty array if disabled / not applicable).
        let stripPrefix: [String] = opts.stripCommonPackagePrefix
            ? commonPackagePrefix(of: doc.classes)
            : []

        // Build the resolution context the .pyi emitter uses to decide
        // between cross-file imports, same-file forward refs, and external
        // forward-declared stubs.
        let topLevelFqcns = Swift.Set(doc.classes.map { $0.fqcn })
        var allFqcns = Swift.Set<String>()
        func collectFqcns(_ c: ClassNode) {
            allFqcns.insert(c.fqcn)
            for n in c.nested { collectFqcns(n) }
        }
        for c in doc.classes { collectFqcns(c) }
        let modulePath: (String) -> String? = { fqcn in
            guard topLevelFqcns.contains(fqcn) else { return nil }
            let pkg = self.packageParts(of: fqcn, stripping: stripPrefix)
            let simple = fqcn.split(separator: ".").last.map(String.init) ?? fqcn
            return (pkg + [simple]).joined(separator: ".")
        }
        let resolution = PyiStubEmitter.Resolution(
            topLevelFqcns: topLevelFqcns,
            allFqcns: allFqcns,
            modulePath: modulePath,
            externalModules: opts.externalModules
        )

        switch opts.fileLayout {
        case .perClass:
            var packagesTouched = Swift.Set<URL>()
            for cls in doc.classes {
                let module = emitter.module(for: cls)
                let code = generatePythonCode(from: module)
                let pkgParts = packageParts(of: cls.fqcn, stripping: stripPrefix)
                var dir = opts.outputDir
                for part in pkgParts {
                    dir.appendPathComponent(part)
                    packagesTouched.insert(dir)
                }
                try FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
                let file = dir.appendingPathComponent("\(cls.simpleName).py")
                try code.write(to: file, atomically: true, encoding: .utf8)
                written.append(file)

                // Companion .pyi stub with Pythonic types.
                let stub = pyiEmitter.render(cls, resolution: resolution)
                let stubFile = dir.appendingPathComponent("\(cls.simpleName).pyi")
                try stub.write(to: stubFile, atomically: true, encoding: .utf8)
                written.append(stubFile)
            }
            // Ensure every package on the path has an __init__.py
            for dir in packagesTouched {
                let initFile = dir.appendingPathComponent("__init__.py")
                if !FileManager.default.fileExists(atPath: initFile.path) {
                    try "".write(to: initFile, atomically: true, encoding: .utf8)
                    written.append(initFile)
                }
            }

        case .singleFile:
            var body: [Statement] = [.importFrom(.init(
                module: "jnius",
                names: [
                    Alias(name: "JavaClass", asName: nil),
                    Alias(name: "JavaInterface", asName: nil),
                    Alias(name: "MetaJavaClass", asName: nil),
                    Alias(name: "JavaMethod", asName: nil),
                    Alias(name: "JavaStaticMethod", asName: nil),
                    Alias(name: "JavaMultipleMethod", asName: nil),
                    Alias(name: "JavaField", asName: nil),
                    Alias(name: "JavaStaticField", asName: nil),
                ],
                level: 0
            ))]
            for cls in doc.classes {
                body.append(.blank(.init(count: 1)))
                body.append(.classDef(emitter.classDef(for: cls)))
            }
            let code = generatePythonCode(from: .module(body))
            let file = opts.outputDir.appendingPathComponent("wrappers.py")
            try code.write(to: file, atomically: true, encoding: .utf8)
            written.append(file)
        }
        return written
    }

    private func packageParts(of fqcn: String,
                              stripping prefix: [String] = []) -> [String] {
        let parts = fqcn.split(separator: ".").map(String.init)
        if parts.count <= 1 { return [] }
        var pkg = Array(parts.dropLast())
        if !prefix.isEmpty,
           pkg.count >= prefix.count,
           Array(pkg.prefix(prefix.count)) == prefix {
            pkg.removeFirst(prefix.count)
        }
        return pkg
    }

    /// Longest common package prefix (as ordered segments) across all
    /// top-level classes. Returns `[]` when fewer than two classes exist
    /// or when nothing meaningful is shared.
    private func commonPackagePrefix(of classes: [ClassNode]) -> [String] {
        var pkgs: [[String]] = []
        for cls in classes {
            let parts = cls.fqcn.split(separator: ".").map(String.init)
            guard parts.count > 1 else { return [] }
            pkgs.append(Array(parts.dropLast()))
        }
        guard let first = pkgs.first else { return [] }
        var prefix = first
        for pkg in pkgs.dropFirst() {
            var i = 0
            let limit = Swift.min(prefix.count, pkg.count)
            while i < limit && prefix[i] == pkg[i] { i += 1 }
            prefix = Array(prefix.prefix(i))
            if prefix.isEmpty { return [] }
        }
        return prefix
    }

    private func invokeJar(opts: Options) throws -> Data {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/env")
        process.arguments = [
            opts.javaExecutable,
            "-jar", opts.jarPath.path,
            opts.inputDir.path,
        ]
        let stdoutPipe = Pipe()
        let stderrPipe = Pipe()
        process.standardOutput = stdoutPipe
        process.standardError = stderrPipe
        try process.run()
        // Drain pipes concurrently to avoid blocking the child on a full pipe
        // buffer (macOS default is ~64KB; large ASTs easily exceed this).
        var stdout = Data()
        var stderr = Data()
        let group = DispatchGroup()
        let queue = DispatchQueue(label: "pyjnius-wrap.pipe-drain", attributes: .concurrent)
        group.enter()
        queue.async {
            stdout = stdoutPipe.fileHandleForReading.readDataToEndOfFile()
            group.leave()
        }
        group.enter()
        queue.async {
            stderr = stderrPipe.fileHandleForReading.readDataToEndOfFile()
            group.leave()
        }
        process.waitUntilExit()
        group.wait()
        if process.terminationStatus != 0 {
            throw PipelineError.javaFailed(
                exitCode: process.terminationStatus,
                stderr: String(data: stderr, encoding: .utf8) ?? ""
            )
        }
        return stdout
    }
}

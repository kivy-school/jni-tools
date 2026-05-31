// CythonEmitter pipeline. Mirrors JniWrapCore.Pipeline but routes the
// per-class rendering through CythonClassEmitter + CythonPxdEmitter, and
// reuses PyiStubEmitter unchanged for the `.pyi` stubs.

import Foundation
import JniWrapCore

/// Pipeline that turns an `AstDocument` into a per-class Cython package on
/// disk: `Foo.pyx` + `Foo.pxd` + `Foo.pyi` per class, with `__init__.py`
/// shells at every package level.
public struct CythonPipeline: Sendable {
    public struct Options: Sendable {
        public var inputDir: URL
        public var outputDir: URL
        /// Python module path to cimport the runtime from. Defaults to
        /// the shipped package name `jni_core`.
        public var jniCoreImport: String
        /// When true, flatten output into a single `wrappers.pyx`/`.pxd`/`.pyi`.
        public var singleFile: Bool
        /// When true, merge all classes in the same Java package into a single
        /// `.pyx`/`.pxd`/`.pyi` file (e.g. `language.pyx` instead of
        /// `language/LanguageContext.pyx`). Takes precedence over `singleFile`.
        public var perPackage: Bool
        /// When true, strip the longest common reverse-DNS package prefix
        /// from emitted module paths (mirrors `Pipeline.Options`).
        public var stripCommonPackagePrefix: Bool

        public init(inputDir: URL,
                    outputDir: URL,
                    jniCoreImport: String = "jni_core",
                    singleFile: Bool = false,
                    perPackage: Bool = false,
                    stripCommonPackagePrefix: Bool = true) {
            self.inputDir = inputDir
            self.outputDir = outputDir
            self.jniCoreImport = jniCoreImport
            self.singleFile = singleFile
            self.perPackage = perPackage
            self.stripCommonPackagePrefix = stripCommonPackagePrefix
        }
    }

    public enum CythonEmitterError: Error, CustomStringConvertible {
        case notImplemented(String)

        public var description: String {
            switch self {
            case .notImplemented(let what):
                return "Cython emitter: \(what) not implemented yet."
            }
        }
    }

    public init() {}

    public func emit(doc: AstDocument, opts: Options) throws -> [URL] {
        let classEmitter = CythonClassEmitter()
        let pxdEmitter = CythonPxdEmitter()
        let pyiEmitter = PyiStubEmitter()
        try FileManager.default.createDirectory(at: opts.outputDir,
                                                withIntermediateDirectories: true)
        var written: [URL] = []

        let stripPrefix: [String] = opts.stripCommonPackagePrefix
            ? commonPackagePrefix(of: doc.classes)
            : []

        // Build the resolution context the .pyi emitter uses (same shape
        // as JniWrapCore.Pipeline.emit — copied because Pipeline keeps
        // these as private helpers).
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
            externalModules: []
        )
        let pyxOptions = CythonClassEmitter.Options(jniCoreImport: opts.jniCoreImport)

        if opts.perPackage {
            // Group classes by their package path, emit one .pyx/.pxd/.pyi per package.
            var byPackage: [([String], [ClassNode])] = []
            var pkgIndex: [[String]: Int] = [:]
            for cls in doc.classes {
                let pkg = packageParts(of: cls.fqcn, stripping: stripPrefix)
                if let idx = pkgIndex[pkg] {
                    byPackage[idx].1.append(cls)
                } else {
                    pkgIndex[pkg] = byPackage.count
                    byPackage.append((pkg, [cls]))
                }
            }
            for (pkgParts, classes) in byPackage {
                var dir = opts.outputDir
                for part in pkgParts.dropLast() {
                    dir.appendPathComponent(part)
                    try FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
                    let initFile = dir.appendingPathComponent("__init__.py")
                    if !FileManager.default.fileExists(atPath: initFile.path) {
                        try "".write(to: initFile, atomically: true, encoding: .utf8)
                        written.append(initFile)
                    }
                }
                let moduleName = pkgParts.last ?? "wrappers"
                let pyxParts = classes.enumerated().map { (i, cls) -> String in
                    let rendered = classEmitter.renderPyx(cls, options: pyxOptions)
                    return i == 0 ? rendered : stripCythonHeader(rendered)
                }
                let pxdParts = classes.enumerated().map { (i, cls) -> String in
                    let rendered = classEmitter.renderPxd(cls, options: pyxOptions)
                    return i == 0 ? rendered : stripPxdHeader(rendered)
                }
                let pyxFile = dir.appendingPathComponent("\(moduleName).pyx")
                try pyxParts.joined(separator: "\n").write(to: pyxFile, atomically: true, encoding: .utf8)
                written.append(pyxFile)
                let pxdFile = dir.appendingPathComponent("\(moduleName).pxd")
                try pxdParts.joined(separator: "\n").write(to: pxdFile, atomically: true, encoding: .utf8)
                written.append(pxdFile)
                var pyiBuf = ""
                for cls in classes {
                    pyiBuf += pyiEmitter.render(cls, resolution: resolution)
                    pyiBuf += "\n"
                }
                let pyiFile = dir.appendingPathComponent("\(moduleName).pyi")
                try pyiBuf.write(to: pyiFile, atomically: true, encoding: .utf8)
                written.append(pyiFile)
            }
            return written
        }

        if opts.singleFile {
            // Flatten everything into wrappers.pyx + wrappers.pxd + wrappers.pyi.
            var pyxParts: [String] = []
            var pxdParts: [String] = []
            for (i, cls) in doc.classes.enumerated() {
                let pyx = classEmitter.renderPyx(cls, options: pyxOptions)
                let pxd = classEmitter.renderPxd(cls, options: pyxOptions)
                if i == 0 {
                    pyxParts.append(pyx)
                    pxdParts.append(pxd)
                } else {
                    pyxParts.append(stripCythonHeader(pyx))
                    pxdParts.append(stripPxdHeader(pxd))
                }
            }
            let pyxFile = opts.outputDir.appendingPathComponent("wrappers.pyx")
            try pyxParts.joined(separator: "\n").write(to: pyxFile, atomically: true, encoding: .utf8)
            written.append(pyxFile)
            let pxdFile = opts.outputDir.appendingPathComponent("wrappers.pxd")
            try pxdParts.joined(separator: "\n").write(to: pxdFile, atomically: true, encoding: .utf8)
            written.append(pxdFile)
            var pyiBuf = ""
            for cls in doc.classes {
                pyiBuf += pyiEmitter.render(cls, resolution: resolution)
                pyiBuf += "\n"
            }
            let pyiFile = opts.outputDir.appendingPathComponent("wrappers.pyi")
            try pyiBuf.write(to: pyiFile, atomically: true, encoding: .utf8)
            written.append(pyiFile)
            return written
        }

        // perClass layout.
        var packagesTouched = Swift.Set<URL>()
        for cls in doc.classes {
            let pkgParts = packageParts(of: cls.fqcn, stripping: stripPrefix)
            var dir = opts.outputDir
            for part in pkgParts {
                dir.appendPathComponent(part)
                packagesTouched.insert(dir)
            }
            try FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)

            let pyxFile = dir.appendingPathComponent("\(cls.simpleName).pyx")
            try classEmitter.renderPyx(cls, options: pyxOptions)
                .write(to: pyxFile, atomically: true, encoding: .utf8)
            written.append(pyxFile)

            let pxdFile = dir.appendingPathComponent("\(cls.simpleName).pxd")
            try classEmitter.renderPxd(cls, options: pyxOptions)
                .write(to: pxdFile, atomically: true, encoding: .utf8)
            written.append(pxdFile)

            let pyiFile = dir.appendingPathComponent("\(cls.simpleName).pyi")
            try pyiEmitter.render(cls, resolution: resolution)
                .write(to: pyiFile, atomically: true, encoding: .utf8)
            written.append(pyiFile)
        }
        for dir in packagesTouched {
            let initFile = dir.appendingPathComponent("__init__.py")
            if !FileManager.default.fileExists(atPath: initFile.path) {
                try "".write(to: initFile, atomically: true, encoding: .utf8)
                written.append(initFile)
            }
        }
        return written
    }

    // MARK: - Helpers (duplicated from Pipeline.swift — kept private there)

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

    /// Drop the leading directive + cimport block + `include` line from a
    /// rendered `.pyx` so concatenated output keeps a single header.
    private func stripCythonHeader(_ source: String) -> String {
        let lines = source.split(separator: "\n", omittingEmptySubsequences: false)
        var i = 0
        var sawConversions = false
        while i < lines.count {
            if lines[i].contains("conversions.pxi\"") {
                sawConversions = true
                i += 1
                break
            }
            i += 1
        }
        if !sawConversions { return source }
        while i < lines.count && lines[i].trimmingCharacters(in: .whitespaces).isEmpty {
            i += 1
        }
        return lines[i..<lines.count].joined(separator: "\n")
    }

    /// Drop the cython directive + JavaObject cimport from a `.pxd` so
    /// concatenated output keeps a single header.
    private func stripPxdHeader(_ source: String) -> String {
        let lines = source.split(separator: "\n", omittingEmptySubsequences: false)
        var i = 0
        while i < lines.count {
            if lines[i].contains("cimport JavaObject") { i += 1; break }
            i += 1
        }
        while i < lines.count && lines[i].trimmingCharacters(in: .whitespaces).isEmpty {
            i += 1
        }
        return lines[i..<lines.count].joined(separator: "\n")
    }
}

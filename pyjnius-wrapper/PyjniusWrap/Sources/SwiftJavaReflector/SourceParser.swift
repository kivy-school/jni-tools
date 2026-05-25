import Foundation
import PyjniusWrapCore
import SwiftJava
import JavaLangReflect

/// Parses Java source files using JavaParser (called from Swift via swift-java),
/// producing `[ClassNode]` compatible with `PyjniusWrapCore.Schema`.
///
/// This replaces the subprocess invocation of `java-ast-emitter.jar` by calling
/// the same Java classes (`ClassExtractor`, `JavaAstEmitter`) directly in-process
/// through swift-java's embedded JVM. The java-ast-emitter JAR is loaded onto the
/// JVM classpath, and its `JavaAstEmitter.processDirectory()` / `ClassExtractor`
/// logic is invoked from Swift — no subprocess, no piped stdout, no shell.
///
/// This gives us:
/// - Javadoc extraction (from source files)
/// - Proper parameter names (from source)
/// - Full symbol resolution via JavaParser's symbol solver
/// - No Gradle build step needed at _runtime_ — just the pre-built JAR on classpath
///
/// Requirements:
/// - The `java-ast-emitter.jar` (shadow/fat JAR with JavaParser + ASM + Jackson bundled)
///   must be available — either bundled as a resource or passed explicitly.
/// - JDK 17+ on PATH (swift-java embeds the JVM in-process).
public struct SourceParser: Sendable {

    /// Configuration for the source parser.
    public struct Config: Sendable {
        /// Path to the directory containing `.java` source files, or a JAR/AAR/class directory.
        public var inputPath: URL
        /// Additional classpath entries for symbol resolution (e.g., dependent JARs).
        public var additionalClasspath: [URL]
        /// Path to the java-ast-emitter fat JAR. If nil, uses the bundled resource.
        public var emitterJarPath: URL?

        public init(inputPath: URL, additionalClasspath: [URL] = [],
                    emitterJarPath: URL? = nil) {
            self.inputPath = inputPath
            self.additionalClasspath = additionalClasspath
            self.emitterJarPath = emitterJarPath
        }
    }

    public init() {}

    /// Parses all `.java` files (or bytecode artifacts) in the configured input path
    /// and returns an `AstDocument`.
    ///
    /// Calls the Java `JavaAstEmitter` class in-process via swift-java. The emitter
    /// auto-detects whether the input contains source files or compiled artifacts and
    /// uses JavaParser or ASM accordingly. The result is captured as JSON in-memory
    /// and decoded into our Swift schema.
    public func parse(config: Config) throws -> AstDocument {
        let emitterJar = try resolveEmitterJar(config.emitterJarPath)
        let classpath = buildClasspath(emitterJar: emitterJar, additional: config.additionalClasspath)

        // Boot the embedded JVM with the emitter JAR (contains JavaParser, ASM, Jackson).
        let jvm = try JavaVirtualMachine.shared(classpath: classpath)
        let environment = try jvm.environment()

        // Call JavaAstEmitter.emitJson(String inputPath) → String (JSON)
        // This is a static helper method we add to the emitter that returns the JSON
        // string directly instead of printing to stdout.
        let json = try invokeEmitter(inputPath: config.inputPath.path, environment: environment)

        guard let data = json.data(using: .utf8), !data.isEmpty else {
            return AstDocument(classes: [])
        }

        do {
            return try JSONDecoder().decode(AstDocument.self, from: data)
        } catch {
            throw SourceParserError.parseError("Failed to decode AST JSON: \(error)")
        }
    }

    // MARK: - Private Helpers

    private func resolveEmitterJar(_ explicit: URL?) throws -> URL {
        if let explicit { return explicit }
        // Look for bundled java-ast-emitter JAR — same one the legacy subprocess uses.
        if let url = Bundle.main.url(forResource: "java-ast-emitter", withExtension: "jar") {
            return url
        }
        // Try the module bundle (SwiftPM resource).
        if let url = Bundle.module.url(forResource: "java-ast-emitter", withExtension: "jar") {
            return url
        }
        throw SourceParserError.emitterJarNotFound(
            "java-ast-emitter.jar not found. Pass --jar explicitly or ensure it is bundled as a resource.")
    }

    private func buildClasspath(emitterJar: URL, additional: [URL]) -> [String] {
        var entries = [emitterJar.path]
        entries.append(contentsOf: additional.map(\.path))
        return entries
    }

    /// Invokes the Java emitter in-process via swift-java to get JSON output.
    ///
    /// Strategy: We call the emitter's main class with a custom approach:
    /// 1. Load `JavaAstEmitter` class from the fat JAR
    /// 2. Call its `emitJson(String)` static method (added as a convenience entrypoint)
    ///    OR fall back to capturing stdout from `main(String[])` if the method isn't available.
    private func invokeEmitter(inputPath: String, environment: JNIEnvironment) throws -> String {
        let emitterClass = try JavaClass.forName(
            "dev.kivyschool.pyjniuswrap.JavaAstEmitter", environment: environment)

        // Try the direct emitJson method first (preferred — no stdout redirect needed).
        do {
            let emitMethod = emitterClass.getDeclaredMethods().first { method in
                method.getName() == "emitJson" &&
                method.getParameterCount() == 1
            }
            if let emitMethod {
                emitMethod.setAccessible(true)
                let javaInputPath = try JavaString(inputPath, environment: environment)
                let result = emitMethod.invoke(nil, args: [javaInputPath])
                if let jsonStr = result?.toString() {
                    return jsonStr
                }
            }
        } catch {
            // Fall through to stdout capture approach.
        }

        // Fallback: Redirect System.out to a ByteArrayOutputStream, call main(),
        // then restore System.out and read the captured bytes.
        return try captureMainOutput(emitterClass: emitterClass,
                                     inputPath: inputPath,
                                     environment: environment)
    }

    /// Captures stdout from JavaAstEmitter.main() by temporarily redirecting System.out.
    private func captureMainOutput(emitterClass: JavaClass<JavaObject>,
                                   inputPath: String,
                                   environment: JNIEnvironment) throws -> String {
        // java.io.ByteArrayOutputStream baos = new ByteArrayOutputStream();
        let baosClass = try JavaClass.forName("java.io.ByteArrayOutputStream", environment: environment)
        let printStreamClass = try JavaClass.forName("java.io.PrintStream", environment: environment)
        let systemClass = try JavaClass.forName("java.lang.System", environment: environment)

        // Get current System.out
        let outField = systemClass.getDeclaredField("out")
        let originalOut = outField.get(nil)

        // Create ByteArrayOutputStream and wrap in PrintStream
        let baosConstructor = baosClass.getDeclaredConstructor(parameterTypes: [])
        let baos = try baosConstructor.newInstance(args: [])

        let psConstructor = printStreamClass.getDeclaredConstructors().first { ctor in
            let params = ctor.getParameterTypes()
            return params.count == 1 && params[0].getName() == "java.io.OutputStream"
        }
        guard let psConstructor else {
            throw SourceParserError.parseError("Cannot find PrintStream(OutputStream) constructor")
        }
        let printStream = try psConstructor.newInstance(args: [baos])

        // Redirect System.out
        let setOutMethod = systemClass.getDeclaredMethods().first { m in
            m.getName() == "setOut" && m.getParameterCount() == 1
        }
        guard let setOutMethod else {
            throw SourceParserError.parseError("Cannot find System.setOut method")
        }
        try setOutMethod.invoke(nil, args: [printStream])

        // Call JavaAstEmitter.main(new String[]{inputPath})
        defer {
            // Restore original System.out (if it was non-nil).
            if let originalOut {
                try? setOutMethod.invoke(nil, args: [originalOut])
            }
        }

        let mainMethod = emitterClass.getDeclaredMethods().first { m in
            m.getName() == "main" && m.getParameterCount() == 1
        }
        guard let mainMethod else {
            throw SourceParserError.parseError("Cannot find JavaAstEmitter.main(String[]) method")
        }

        // Create String[] with the input path and invoke main.
        let argsArray = JavaArray<JavaObject>(count: 1, environment: environment)
        argsArray[0] = try JavaString(inputPath, environment: environment)
        try mainMethod.invoke(nil, args: [argsArray])

        // Flush and read captured output
        let flushMethod = printStream.getClass().getDeclaredMethods().first { m in
            m.getName() == "flush" && m.getParameterCount() == 0
        }
        try flushMethod?.invoke(printStream, args: [])

        let toStringMethod = baos.getClass().getDeclaredMethods().first { m in
            m.getName() == "toString" && m.getParameterCount() == 0
        }
        guard let toStringMethod else {
            throw SourceParserError.parseError("Cannot find ByteArrayOutputStream.toString()")
        }
        let output = try toStringMethod.invoke(baos, args: [])
        return output?.toString() ?? ""
    }
}

// MARK: - Errors

public enum SourceParserError: Error, CustomStringConvertible {
    case emitterJarNotFound(String)
    case parseError(String)
    case symbolResolutionFailed(String)

    public var description: String {
        switch self {
        case .emitterJarNotFound(let msg):
            return msg
        case .parseError(let msg):
            return "Source parser error: \(msg)"
        case .symbolResolutionFailed(let msg):
            return "Symbol resolution failed: \(msg)"
        }
    }
}


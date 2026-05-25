import Foundation
import PyjniusWrapCore

/// Reflects on Java classes in a JAR/AAR file using an embedded JVM (via swift-java)
/// to produce a `PyjniusWrapCore.AstDocument`.
///
/// **Status:** STUB. The real implementation will:
///   1. Boot the embedded JVM with the target JAR on the classpath via
///      `try JavaVirtualMachine.shared(classpath: [...])`.
///   2. Enumerate `.class` entries using `JarFile.entries()` from the
///      `JavaUtilJar` product.
///   3. For each class name, load it with
///      `try JavaClass<JavaObject>.forName("com.example.Foo", environment: env)`
///      and walk `getDeclaredFields()` / `getDeclaredConstructors()`
///      / `getDeclaredMethods()` / `getDeclaredClasses()` (from
///      `JavaLangReflect`) to populate a `ClassNode`.
///
/// Today `reflect(config:)` throws `ReflectorError.notImplemented` — wire
/// the swift-java dependency into `Package.swift` and implement the body
/// before relying on it from the CLI.
public struct Reflector: Sendable {

    /// Configuration for the reflector.
    public struct Config: Sendable {
        /// Path to the JAR or AAR file to reflect on.
        public var inputPath: URL
        /// Additional classpath entries (e.g., dependent JARs).
        public var additionalClasspath: [URL]

        public init(inputPath: URL, additionalClasspath: [URL] = []) {
            self.inputPath = inputPath
            self.additionalClasspath = additionalClasspath
        }
    }

    public init() {}

    /// Reflects on all classes in the given JAR/AAR and returns an `AstDocument`.
    public func reflect(config: Config) throws -> AstDocument {
        throw ReflectorError.notImplemented(
            "Reflector.reflect is not yet implemented. The swift-java in-process JVM " +
            "integration is being built — see Sources/SwiftJavaReflector/Reflector.swift " +
            "and Package.swift for the wiring TODOs."
        )
    }
}

// MARK: - Errors

public enum ReflectorError: Error, CustomStringConvertible {
    case notImplemented(String)
    case noClassesJarInAar(String)
    case jvmBootFailed(String)
    case classLoadFailed(String, underlying: Error)

    public var description: String {
        switch self {
        case .notImplemented(let msg):
            return "Reflector not implemented: \(msg)"
        case .noClassesJarInAar(let path):
            return "No classes.jar found in AAR: \(path)"
        case .jvmBootFailed(let msg):
            return "Failed to boot embedded JVM: \(msg)"
        case .classLoadFailed(let className, let err):
            return "Failed to load class '\(className)': \(err)"
        }
    }
}

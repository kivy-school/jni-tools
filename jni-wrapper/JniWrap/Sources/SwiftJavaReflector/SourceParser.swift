import Foundation
import JniWrapCore

/// Parses Java source files in-process to produce a `JniWrapCore.AstDocument`.
///
/// **Status:** STUB. The intended design is to call the JavaParser library
/// directly through swift-java (no custom Java code, no subprocess). That
/// requires either:
///   (a) swift-java bindings generated for `com.github.javaparser.*` via
///       the `swift-java wrap-java` tool / `SwiftJavaPlugin`, OR
///   (b) a thin in-process bridge that walks the JavaParser AST through
///       `JavaLangReflect`.
///
/// Today `parse(config:)` throws `SourceParserError.notImplemented`.
public struct SourceParser: Sendable {

    /// Configuration for the source parser.
    public struct Config: Sendable {
        /// Path to the directory containing `.java` source files.
        public var inputPath: URL
        /// Additional classpath entries for symbol resolution (e.g., dependent JARs).
        public var additionalClasspath: [URL]
        /// Path to a JAR containing JavaParser and its dependencies.
        /// If nil, JavaParser must already be on the JVM classpath.
        public var javaParserJarPath: URL?

        public init(inputPath: URL,
                    additionalClasspath: [URL] = [],
                    javaParserJarPath: URL? = nil) {
            self.inputPath = inputPath
            self.additionalClasspath = additionalClasspath
            self.javaParserJarPath = javaParserJarPath
        }
    }

    public init() {}

    /// Parses all `.java` files in the configured input path and returns an `AstDocument`.
    public func parse(config: Config) throws -> AstDocument {
        throw SourceParserError.notImplemented(
            "SourceParser.parse is not yet implemented. The JavaParser-via-swift-java " +
            "integration is being built — see Sources/SwiftJavaReflector/SourceParser.swift."
        )
    }
}

// MARK: - Errors

public enum SourceParserError: Error, CustomStringConvertible {
    case notImplemented(String)
    case parseError(String)
    case symbolResolutionFailed(String)

    public var description: String {
        switch self {
        case .notImplemented(let msg):
            return "SourceParser not implemented: \(msg)"
        case .parseError(let msg):
            return "Source parser error: \(msg)"
        case .symbolResolutionFailed(let msg):
            return "Symbol resolution failed: \(msg)"
        }
    }
}

import ArgumentParser
import Foundation
import PyjniusWrapCore
import SwiftJavaReflector
import CythonEmitter

@main
struct PyjniusWrap: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "pyjnius-wrap",
        abstract: "Generate Python wrappers from Java sources / JAR / AAR files.",
        subcommands: [PyjniusCmd.self, CythonCmd.self],
        defaultSubcommand: PyjniusCmd.self
    )
}

// MARK: - Shared option groups

/// Options that pick which AST extractor to run. Both subcommands accept
/// these — what changes is the emitter that consumes the resulting AST.
struct ExtractionOptions: ParsableArguments {
    @Argument(help: "Folder containing .java source files, or a .jar/.aar file to scan.")
    var inputDir: String

    @Argument(help: "Destination folder for generated files.")
    var outputDir: String

    @Option(name: .long,
            help: "Path to a JAR containing JavaParser and its dependencies (used by the 'source' backend).")
    var javaParserJar: String?

    @Option(name: .long,
            help: "Extraction backend: 'swift-java' (default, embedded JVM reflection for bytecode/JAR/AAR) or 'source' (JavaParser via swift-java for .java source files with javadoc).")
    var backend: String = "swift-java"

    func extract() throws -> (AstDocument, URL, URL) {
        let inURL = URL(fileURLWithPath: inputDir)
        let outURL = URL(fileURLWithPath: outputDir)
        let parsed = try parsedBackend()
        let doc: AstDocument
        switch parsed {
        case .swiftJava:
            doc = try Reflector().reflect(config: .init(inputPath: inURL))
        case .source:
            let jarURL: URL? = javaParserJar.map { URL(fileURLWithPath: $0) }
            doc = try SourceParser().parse(config: .init(
                inputPath: inURL,
                javaParserJarPath: jarURL
            ))
        }
        return (doc, inURL, outURL)
    }

    /// Returns the parsed backend for callers that need to thread it through
    /// to the emitter pipeline.
    func parsedBackend() throws -> Pipeline.Backend {
        guard let b = Pipeline.Backend(rawValue: backend) else {
            throw ValidationError("Invalid backend '\(backend)'. Use 'swift-java' or 'source'.")
        }
        return b
    }
}

/// Shared layout-shaping flags (used by both subcommands).
struct LayoutOptions: ParsableArguments {
    @Flag(name: .long, help: "Flatten output into a single file.")
    var singleFile: Bool = false

    @Flag(name: .long,
          help: "Keep the full Java reverse-DNS package path. Default: strip the longest common prefix.")
    var keepPackagePrefix: Bool = false
}

// MARK: - pyjnius subcommand (existing behaviour preserved verbatim)

struct PyjniusCmd: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "pyjnius",
        abstract: "Generate pyjnius wrapper modules (current default behaviour)."
    )

    @OptionGroup var extraction: ExtractionOptions
    @OptionGroup var layout: LayoutOptions

    @Option(name: .customLong("external-module"),
            parsing: .singleValue,
            help: ArgumentHelp(
                "Map a Java package prefix to an existing Python module so its classes are imported instead of stubbed (repeatable).",
                discussion: "Form: '<java.prefix.>=<python.prefix>' (e.g. 'android.=android'). When '=<python.prefix>' is omitted, the Java prefix minus its trailing dot is used. The Java prefix MUST end with '.' so 'android.' doesn't accidentally match 'androidx.'."))
    var externalModule: [String] = []

    func run() throws {
        let (doc, inURL, outURL) = try extraction.extract()
        let externals = try parseExternalModules(externalModule)
        let written = try Pipeline().emit(doc: doc, opts: .init(
            inputDir: inURL,
            outputDir: outURL,
            fileLayout: layout.singleFile ? .singleFile : .perClass,
            backend: try extraction.parsedBackend(),
            stripCommonPackagePrefix: !layout.keepPackagePrefix,
            externalModules: externals
        ))
        for url in written { print(url.path) }
    }

    private func parseExternalModules(_ raw: [String])
        throws -> [(javaPrefix: String, pyPrefix: String)] {
        var result: [(String, String)] = []
        for entry in raw {
            let parts = entry.split(separator: "=", maxSplits: 1,
                                    omittingEmptySubsequences: false)
            let javaPrefix = String(parts[0])
            let pyPrefix: String
            if parts.count == 2 {
                pyPrefix = String(parts[1])
            } else {
                pyPrefix = javaPrefix.hasSuffix(".")
                    ? String(javaPrefix.dropLast())
                    : javaPrefix
            }
            guard javaPrefix.hasSuffix(".") else {
                throw ValidationError(
                    "--external-module Java prefix '\(javaPrefix)' must end with '.' (e.g. 'android.') so it cannot accidentally match adjacent namespaces like 'androidx.'.")
            }
            guard !pyPrefix.isEmpty else {
                throw ValidationError(
                    "--external-module Python prefix for '\(javaPrefix)' is empty.")
            }
            result.append((javaPrefix, pyPrefix))
        }
        return result
    }
}

// MARK: - cython subcommand (new — Phase 3 fills in the emitter)

struct CythonCmd: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "cython",
        abstract: "Generate Cython modules (.pyx/.pxd/.pyi) that call JNI directly via jni_core."
    )

    @OptionGroup var extraction: ExtractionOptions
    @OptionGroup var layout: LayoutOptions

    @Option(name: .long,
            help: "Python module path to cimport the runtime from (default: jni_core).")
    var jniCoreImport: String = "jni_core"

    func run() throws {
        let (doc, inURL, outURL) = try extraction.extract()
        let written = try CythonPipeline().emit(doc: doc, opts: .init(
            inputDir: inURL,
            outputDir: outURL,
            jniCoreImport: jniCoreImport,
            singleFile: layout.singleFile,
            stripCommonPackagePrefix: !layout.keepPackagePrefix
        ))
        for url in written { print(url.path) }
    }
}

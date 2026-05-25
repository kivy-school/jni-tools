import ArgumentParser
import Foundation
import PyjniusWrapCore
import SwiftJavaReflector

@main
struct PyjniusWrap: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "pyjnius-wrap",
        abstract: "Generate pyjnius wrapper modules from Java sources."
    )

    @Argument(help: "Folder containing .java source files, or a .jar/.aar file to scan.")
    var inputDir: String

    @Argument(help: "Destination folder for generated Python files.")
    var outputDir: String

    @Option(name: .long, help: "Override the bundled java-ast-emitter.jar path.")
    var jar: String?

    @Option(name: .long, help: "Override the java executable.")
    var javaExecutable: String = "java"

    @Option(name: .long, help: "Extraction backend: 'java' (default, uses java-ast-emitter subprocess) or 'swift-java' (embedded JVM reflection, no Gradle needed).")
    var backend: String = "java"

    @Flag(name: .long, help: "Flatten output into a single wrappers.py file.")
    var singleFile: Bool = false

    @Flag(name: .long,
          help: "Keep the full Java reverse-DNS package path (e.g. com/google/android/gms/ads/MobileAds.py). Default: strip the longest common prefix for a shorter, more Pythonic layout.")
    var keepPackagePrefix: Bool = false

    @Option(name: .customLong("external-module"),
            parsing: .singleValue,
            help: ArgumentHelp(
                "Map a Java package prefix to an existing Python module so its classes are imported instead of stubbed (repeatable).",
                discussion: "Form: '<java.prefix.>=<python.prefix>' (e.g. 'android.=android'). When '=<python.prefix>' is omitted, the Java prefix minus its trailing dot is used. The Java prefix MUST end with '.' so 'android.' doesn't accidentally match 'androidx.'."))
    var externalModule: [String] = []

    func run() throws {
        let inURL = URL(fileURLWithPath: inputDir)
        let outURL = URL(fileURLWithPath: outputDir)

        guard let parsedBackend = Pipeline.Backend(rawValue: backend) else {
            throw ValidationError("Invalid backend '\(backend)'. Use 'java' or 'swift-java'.")
        }

        let externals = try parseExternalModules(externalModule)

        switch parsedBackend {
        case .java:
            let jarURL: URL
            if let jar { jarURL = URL(fileURLWithPath: jar) }
            else { jarURL = try resolveBundledJar() }

            let pipeline = Pipeline()
            let written = try pipeline.run(.init(
                inputDir: inURL,
                outputDir: outURL,
                jarPath: jarURL,
                javaExecutable: javaExecutable,
                fileLayout: singleFile ? .singleFile : .perClass,
                backend: .java,
                stripCommonPackagePrefix: !keepPackagePrefix,
                externalModules: externals
            ))
            for url in written {
                print(url.path)
            }

        case .swiftJava:
            // Use the embedded JVM reflector — no subprocess needed.
            let reflector = Reflector()
            let config = Reflector.Config(inputPath: inURL)
            let doc = try reflector.reflect(config: config)

            // Emit using the existing pipeline emission logic.
            // We still need a jarPath for the Options struct but it won't be used.
            let pipeline = Pipeline()
            let written = try pipeline.emit(doc: doc, opts: .init(
                inputDir: inURL,
                outputDir: outURL,
                jarPath: inURL, // unused in emit path
                fileLayout: singleFile ? .singleFile : .perClass,
                backend: .swiftJava,
                stripCommonPackagePrefix: !keepPackagePrefix,
                externalModules: externals
            ))
            for url in written {
                print(url.path)
            }
        }
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
                // Default: java prefix minus trailing dot.
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


    private func resolveBundledJar() throws -> URL {
        if let url = Bundle.module.url(forResource: "java-ast-emitter", withExtension: "jar") {
            return url
        }
        throw ValidationError("Bundled java-ast-emitter.jar not found; pass --jar explicitly.")
    }
}

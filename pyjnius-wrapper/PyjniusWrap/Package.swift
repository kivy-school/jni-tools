// swift-tools-version: 6.1
import PackageDescription

let package = Package(
    name: "PyjniusWrap",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "pyjnius-wrap", targets: ["PyjniusWrap"]),
        .library(name: "PyjniusWrapCore", targets: ["PyjniusWrapCore"]),
        .library(name: "SwiftJavaReflector", targets: ["SwiftJavaReflector"]),
    ],
    dependencies: [
        .package(url: "https://github.com/Py-Swift/PySwiftAST.git", branch: "master"),
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.3.0"),
        // NOTE: swift-java dependency is intentionally NOT declared here yet.
        // SwiftJavaReflector ships as a stub target while the in-process JVM
        // implementation (Reflector / SourceParser) is being built out. Once
        // those modules call real swift-java APIs, add:
        //     .package(url: "https://github.com/swiftlang/swift-java.git", branch: "main")
        // and wire the product deps (SwiftJava, JavaLangReflect, JavaUtilJar, JavaNet)
        // into the SwiftJavaReflector target below.
    ],
    targets: [
        .executableTarget(
            name: "PyjniusWrap",
            dependencies: [
                "PyjniusWrapCore",
                "SwiftJavaReflector",
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ]
        ),
        .target(
            name: "PyjniusWrapCore",
            dependencies: [
                .product(name: "PySwiftAST", package: "PySwiftAST"),
                .product(name: "PySwiftCodeGen", package: "PySwiftAST"),
            ]
        ),
        .target(
            name: "SwiftJavaReflector",
            dependencies: [
                "PyjniusWrapCore",
                // Pending: swift-java products
                // .product(name: "SwiftJava", package: "swift-java"),
                // .product(name: "JavaLangReflect", package: "swift-java"),
                // .product(name: "JavaUtilJar", package: "swift-java"),
                // .product(name: "JavaNet", package: "swift-java"),
            ]
        ),
        .testTarget(
            name: "PyjniusWrapCoreTests",
            dependencies: ["PyjniusWrapCore"],
            resources: [
                .copy("Fixtures"),
            ]
        ),
        .testTarget(
            name: "SwiftJavaReflectorTests",
            dependencies: ["SwiftJavaReflector", "PyjniusWrapCore"]
        ),
    ]
)

// swift-tools-version: 6.2
import PackageDescription

let package = Package(
    name: "PyjniusWrap",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "pyjnius-wrap", targets: ["PyjniusWrap"]),
        .library(name: "PyjniusWrapCore", targets: ["PyjniusWrapCore"]),
        .library(name: "SwiftJavaReflector", targets: ["SwiftJavaReflector"]),
        .library(name: "CythonEmitter", targets: ["CythonEmitter"]),
    ],
    dependencies: [
        .package(url: "https://github.com/Py-Swift/PySwiftAST.git", branch: "master"),
        .package(url: "https://github.com/Py-Swift/CySwiftAst.git", branch: "master"),
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.3.0"),
        .package(url: "https://github.com/swiftlang/swift-java.git", from: "0.3.0"),
    ],
    targets: [
        .executableTarget(
            name: "PyjniusWrap",
            dependencies: [
                "PyjniusWrapCore",
                "SwiftJavaReflector",
                "CythonEmitter",
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
                .product(name: "SwiftJava", package: "swift-java"),
                .product(name: "JavaLangReflect", package: "swift-java"),
                .product(name: "JavaUtilJar", package: "swift-java"),
                .product(name: "JavaNet", package: "swift-java"),
            ]
        ),
        .target(
            name: "CythonEmitter",
            dependencies: [
                "PyjniusWrapCore",
                .product(name: "CySwiftAst", package: "CySwiftAst"),
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
        .testTarget(
            name: "CythonEmitterTests",
            dependencies: ["CythonEmitter", "PyjniusWrapCore"],
            resources: [
                .copy("Fixtures"),
            ]
        ),
    ]
)

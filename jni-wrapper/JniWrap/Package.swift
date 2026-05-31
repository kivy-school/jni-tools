// swift-tools-version: 6.2
import PackageDescription

let package = Package(
    name: "JniWrap",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "jni-wrap", targets: ["JniWrap"]),
        .library(name: "JniWrapCore", targets: ["JniWrapCore"]),
        .library(name: "SwiftJavaReflector", targets: ["SwiftJavaReflector"]),
        .library(name: "CythonEmitter", targets: ["CythonEmitter"]),
    ],
    dependencies: [
        .package(url: "https://github.com/Py-Swift/PySwiftAST.git", branch: "master"),
        .package(url: "https://github.com/Py-Swift/CySwiftAst.git", branch: "master"),
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.3.0"),
        .package(url: "https://github.com/swiftlang/swift-java.git", from: "0.4.0"),
    ],
    targets: [
        .executableTarget(
            name: "JniWrap",
            dependencies: [
                "JniWrapCore",
                "SwiftJavaReflector",
                "CythonEmitter",
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ]
        ),
        .target(
            name: "JniWrapCore",
            dependencies: [
                .product(name: "PySwiftAST", package: "PySwiftAST"),
                .product(name: "PySwiftCodeGen", package: "PySwiftAST"),
            ]
        ),
        .target(
            name: "SwiftJavaReflector",
            dependencies: [
                "JniWrapCore",
                .product(name: "SwiftJava", package: "swift-java"),
                .product(name: "JavaLangReflect", package: "swift-java"),
                .product(name: "JavaUtilJar", package: "swift-java"),
                .product(name: "JavaNet", package: "swift-java"),
            ]
        ),
        .target(
            name: "CythonEmitter",
            dependencies: [
                "JniWrapCore",
                .product(name: "CySwiftAst", package: "CySwiftAst"),
            ]
        ),
        .testTarget(
            name: "JniWrapCoreTests",
            dependencies: ["JniWrapCore"],
            resources: [
                .copy("Fixtures"),
            ]
        ),
        .testTarget(
            name: "SwiftJavaReflectorTests",
            dependencies: ["SwiftJavaReflector", "JniWrapCore"]
        ),
        .testTarget(
            name: "CythonEmitterTests",
            dependencies: ["CythonEmitter", "JniWrapCore"],
            resources: [
                .copy("Fixtures"),
            ]
        ),
    ]
)

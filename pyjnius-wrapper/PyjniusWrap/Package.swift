// swift-tools-version: 6.1
import PackageDescription

let package = Package(
    name: "PyjniusWrap",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "pyjnius-wrap", targets: ["PyjniusWrap"]),
        .library(name: "PyjniusWrapCore", targets: ["PyjniusWrapCore"]),
    ],
    dependencies: [
        .package(url: "https://github.com/Py-Swift/PySwiftAST.git", branch: "master"),
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.3.0"),
    ],
    targets: [
        .executableTarget(
            name: "PyjniusWrap",
            dependencies: [
                "PyjniusWrapCore",
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ],
            resources: [
                .copy("Resources/java-ast-emitter.jar"),
            ]
        ),
        .target(
            name: "PyjniusWrapCore",
            dependencies: [
                .product(name: "PySwiftAST", package: "PySwiftAST"),
                .product(name: "PySwiftCodeGen", package: "PySwiftAST"),
            ]
        ),
        .testTarget(
            name: "PyjniusWrapCoreTests",
            dependencies: ["PyjniusWrapCore"],
            resources: [
                .copy("Fixtures"),
            ]
        ),
    ]
)

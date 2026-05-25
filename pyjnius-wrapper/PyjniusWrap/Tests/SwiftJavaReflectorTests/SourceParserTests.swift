import XCTest
@testable import SwiftJavaReflector
import PyjniusWrapCore

final class SourceParserTests: XCTestCase {

    func testConfigInitialization() {
        let url = URL(fileURLWithPath: "/tmp/test-sources")
        let config = SourceParser.Config(inputPath: url)
        XCTAssertEqual(config.inputPath, url)
        XCTAssertTrue(config.additionalClasspath.isEmpty)
        XCTAssertNil(config.javaParserJarPath)
    }

    func testConfigWithExplicitJar() {
        let inputURL = URL(fileURLWithPath: "/tmp/test-sources")
        let jarURL = URL(fileURLWithPath: "/tmp/javaparser-core.jar")
        let config = SourceParser.Config(
            inputPath: inputURL,
            additionalClasspath: [URL(fileURLWithPath: "/tmp/dep.jar")],
            javaParserJarPath: jarURL
        )
        XCTAssertEqual(config.inputPath, inputURL)
        XCTAssertEqual(config.additionalClasspath.count, 1)
        XCTAssertEqual(config.javaParserJarPath, jarURL)
    }

    func testSourceParserErrorDescriptions() {
        let err1 = SourceParserError.parseError("bad syntax")
        XCTAssertTrue(err1.description.contains("bad syntax"))

        let err2 = SourceParserError.symbolResolutionFailed("unresolved")
        XCTAssertTrue(err2.description.contains("unresolved"))
    }

    func testSourceParserCreation() {
        // Verify SourceParser can be instantiated.
        let parser = SourceParser()
        XCTAssertNotNil(parser)
    }
}

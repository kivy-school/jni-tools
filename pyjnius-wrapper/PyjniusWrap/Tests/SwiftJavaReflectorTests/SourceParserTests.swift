import XCTest
@testable import SwiftJavaReflector
import PyjniusWrapCore

final class SourceParserTests: XCTestCase {

    func testConfigInitialization() {
        let url = URL(fileURLWithPath: "/tmp/test-sources")
        let config = SourceParser.Config(inputPath: url)
        XCTAssertEqual(config.inputPath, url)
        XCTAssertTrue(config.additionalClasspath.isEmpty)
        XCTAssertNil(config.emitterJarPath)
    }

    func testConfigWithExplicitJar() {
        let inputURL = URL(fileURLWithPath: "/tmp/test-sources")
        let jarURL = URL(fileURLWithPath: "/tmp/java-ast-emitter.jar")
        let config = SourceParser.Config(
            inputPath: inputURL,
            additionalClasspath: [URL(fileURLWithPath: "/tmp/dep.jar")],
            emitterJarPath: jarURL
        )
        XCTAssertEqual(config.inputPath, inputURL)
        XCTAssertEqual(config.additionalClasspath.count, 1)
        XCTAssertEqual(config.emitterJarPath, jarURL)
    }

    func testSourceParserErrorDescriptions() {
        let err1 = SourceParserError.emitterJarNotFound("not found")
        XCTAssertTrue(err1.description.contains("not found"))

        let err2 = SourceParserError.parseError("bad syntax")
        XCTAssertTrue(err2.description.contains("bad syntax"))

        let err3 = SourceParserError.symbolResolutionFailed("unresolved")
        XCTAssertTrue(err3.description.contains("unresolved"))
    }

    func testSourceParserCreation() {
        // Verify SourceParser can be instantiated.
        let parser = SourceParser()
        XCTAssertNotNil(parser)
    }
}

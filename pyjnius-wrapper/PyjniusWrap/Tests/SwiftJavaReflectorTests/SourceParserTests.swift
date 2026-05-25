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

        let err3 = SourceParserError.notImplemented("pending")
        XCTAssertTrue(err3.description.contains("pending"))
    }

    func testSourceParserCreation() {
        let parser = SourceParser()
        let config = SourceParser.Config(inputPath: URL(fileURLWithPath: "/tmp/x"))
        XCTAssertThrowsError(try parser.parse(config: config)) { error in
            guard case SourceParserError.notImplemented = error else {
                XCTFail("Expected SourceParserError.notImplemented, got \(error)")
                return
            }
        }
    }

    func testReflectorThrowsOnMissingJar() {
        let reflector = Reflector()
        let config = Reflector.Config(inputPath: URL(fileURLWithPath: "/tmp/nonexistent-\(UUID().uuidString).jar"))
        XCTAssertThrowsError(try reflector.reflect(config: config))
    }
}

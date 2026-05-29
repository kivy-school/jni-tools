import Foundation
import XCTest
@testable import JniWrapCore

final class PyWrapperEmitterTests: XCTestCase {

    private func loadPerson() throws -> AstDocument {
        let url = try XCTUnwrap(
            Bundle.module.url(forResource: "person.ast", withExtension: "json", subdirectory: "Fixtures")
        )
        return try JSONDecoder().decode(AstDocument.self, from: Data(contentsOf: url))
    }

    func testEmitContainsExpectedStrings() throws {
        let doc = try loadPerson()
        let tmp = FileManager.default.temporaryDirectory
            .appendingPathComponent("jni-wrap-test-\(UUID().uuidString)")
        defer { try? FileManager.default.removeItem(at: tmp) }

        let written = try Pipeline().emit(doc: doc, opts: .init(
            inputDir: tmp,                 // unused on the emit-only path
            outputDir: tmp,
            fileLayout: .singleFile
        ))
        XCTAssertEqual(written.count, 1)
        let code = try String(contentsOf: written[0], encoding: .utf8)

        // pyjnius wiring boilerplate
        XCTAssertTrue(code.contains("from jnius import"))
        XCTAssertTrue(code.contains("MetaJavaClass"))
        XCTAssertTrue(code.contains("class Person(JavaClass, metaclass=MetaJavaClass):"))

        // __javaclass__ uses slash form
        XCTAssertTrue(code.contains(#"__javaclass__ = "com/example/fixture/Person""#))

        // Constructor list with both overloads
        XCTAssertTrue(code.contains(#"("(Ljava/lang/String;)V", False)"#))
        XCTAssertTrue(code.contains(#"("(Ljava/lang/String;I)V", False)"#))

        // Static field SPECIES
        XCTAssertTrue(code.contains(#"SPECIES = JavaStaticField("Ljava/lang/String;")"#))
        // Instance field name
        XCTAssertTrue(code.contains(#"name = JavaField("Ljava/lang/String;")"#))

        // Overloaded greet -> JavaMultipleMethod
        XCTAssertTrue(code.contains("greet = JavaMultipleMethod"))
        XCTAssertTrue(code.contains(#"("(Ljava/lang/String;)Ljava/lang/String;", False, False)"#))
        XCTAssertTrue(code.contains(#"("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)"#))

        // Static method anonymous -> JavaStaticMethod
        XCTAssertTrue(code.contains(#"anonymous = JavaStaticMethod("()Lcom/example/fixture/Person;")"#))

        // Single-overload instance method getAge -> JavaMethod
        XCTAssertTrue(code.contains(#"getAge = JavaMethod("()I")"#))

        // Varargs addTags
        XCTAssertTrue(code.contains(#"addTags = JavaMethod("([Ljava/lang/String;)V", varargs=True)"#))
    }

    func testPerClassLayoutCreatesPackageDirs() throws {
        let doc = try loadPerson()
        let tmp = FileManager.default.temporaryDirectory
            .appendingPathComponent("jni-wrap-test-\(UUID().uuidString)")
        defer { try? FileManager.default.removeItem(at: tmp) }

        let written = try Pipeline().emit(doc: doc, opts: .init(
            inputDir: tmp,
            outputDir: tmp,
            fileLayout: .perClass,
            stripCommonPackagePrefix: false
        ))
        let paths = written.map { $0.path }
        XCTAssertTrue(paths.contains { $0.hasSuffix("/com/example/fixture/Person.py") })
        XCTAssertTrue(paths.contains { $0.hasSuffix("/com/__init__.py") })
        XCTAssertTrue(paths.contains { $0.hasSuffix("/com/example/__init__.py") })
        XCTAssertTrue(paths.contains { $0.hasSuffix("/com/example/fixture/__init__.py") })
    }
}

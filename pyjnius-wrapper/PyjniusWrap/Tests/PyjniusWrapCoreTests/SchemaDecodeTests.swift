import Foundation
import XCTest
@testable import PyjniusWrapCore

final class SchemaDecodeTests: XCTestCase {

    private func loadDoc() throws -> AstDocument {
        let url = try XCTUnwrap(
            Bundle.module.url(forResource: "person.ast", withExtension: "json", subdirectory: "Fixtures"),
            "person.ast.json must be packaged"
        )
        return try JSONDecoder().decode(AstDocument.self, from: Data(contentsOf: url))
    }

    func testDecodesAllTopLevelClasses() throws {
        let doc = try loadDoc()
        let fqcns = Swift.Set(doc.classes.map(\.fqcn))
        XCTAssertEqual(fqcns, [
            "com.example.fixture.Color",
            "com.example.fixture.Content",
            "com.example.fixture.Listener",
            "com.example.fixture.Person",
        ])
    }

    func testPersonClassNode() throws {
        let doc = try loadDoc()
        let person = try XCTUnwrap(doc.classes.first { $0.fqcn == "com.example.fixture.Person" })
        XCTAssertEqual(person.kind, .classType)
        XCTAssertEqual(person.jniName, "com/example/fixture/Person")
        XCTAssertEqual(person.fields.count, 3)
        XCTAssertEqual(person.constructors.count, 2)
        XCTAssertTrue(person.methods.contains { $0.name == "addTags" && $0.isVarargs })
    }

    func testInterfaceKindAndImplicitStaticField() throws {
        let doc = try loadDoc()
        let listener = try XCTUnwrap(doc.classes.first { $0.fqcn == "com.example.fixture.Listener" })
        XCTAssertEqual(listener.kind, .interfaceType)
        XCTAssertEqual(listener.methods.count, 2)
        let tag = try XCTUnwrap(listener.fields.first)
        XCTAssertEqual(tag.name, "TAG")
        XCTAssertTrue(tag.isStatic, "interface fields are implicitly static")
    }

    func testNestedClass() throws {
        let doc = try loadDoc()
        let content = try XCTUnwrap(doc.classes.first { $0.fqcn == "com.example.fixture.Content" })
        XCTAssertEqual(content.nested.count, 1)
        let builder = content.nested[0]
        XCTAssertEqual(builder.simpleName, "Builder")
        XCTAssertEqual(builder.jniName, "com/example/fixture/Content/Builder")
    }

    func testEnumConstants() throws {
        let doc = try loadDoc()
        let color = try XCTUnwrap(doc.classes.first { $0.fqcn == "com.example.fixture.Color" })
        XCTAssertEqual(color.kind, .enumType)
        XCTAssertEqual(color.enumConstants?.map(\.name), ["RED", "GREEN", "BLUE"])
    }
}

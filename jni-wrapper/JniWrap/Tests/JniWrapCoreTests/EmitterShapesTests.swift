import Foundation
import XCTest
@testable import JniWrapCore

/// Verifies pyjnius-style output for interface, nested, enum class kinds.
final class EmitterShapesTests: XCTestCase {

    private func loadDoc() throws -> AstDocument {
        let url = try XCTUnwrap(
            Bundle.module.url(forResource: "person.ast", withExtension: "json", subdirectory: "Fixtures")
        )
        return try JSONDecoder().decode(AstDocument.self, from: Data(contentsOf: url))
    }

    private func node(_ fqcn: String) throws -> ClassNode {
        let doc = try loadDoc()
        return try XCTUnwrap(doc.classes.first { $0.fqcn == fqcn })
    }

    private func render(_ cls: ClassNode) -> String {
        PyWrapperEmitter().render(cls)
    }

    func testInterfaceUsesJavaInterfaceBase() throws {
        let listener = try node("com.example.fixture.Listener")
        let code = render(listener)
        // pyjnius has no `JavaInterface` symbol; interfaces are projected as
        // plain `JavaClass` subclasses.
        XCTAssertTrue(code.contains("class Listener(JavaClass, metaclass=MetaJavaClass):"))
        XCTAssertFalse(code.contains("JavaInterface"))
        XCTAssertTrue(code.contains(#"__javaclass__ = "com/example/fixture/Listener""#))
        // No __javaconstructor__ on an interface.
        XCTAssertFalse(code.contains("__javaconstructor__"))
        XCTAssertTrue(code.contains(#"onEvent = JavaMethod("(Ljava/lang/String;I)V")"#))
        XCTAssertTrue(code.contains(#"isReady = JavaMethod("()Z")"#))
        // Implicit static field
        XCTAssertTrue(code.contains(#"TAG = JavaStaticField("Ljava/lang/String;")"#))
    }

    func testNestedClassRendersInsideOuter() throws {
        let content = try node("com.example.fixture.Content")
        let code = render(content)
        XCTAssertTrue(code.contains("class Content(JavaClass, metaclass=MetaJavaClass):"))
        XCTAssertTrue(code.contains("class Builder(JavaClass, metaclass=MetaJavaClass):"))
        XCTAssertTrue(code.contains(#"__javaclass__ = "com/example/fixture/Content/Builder""#))
        XCTAssertTrue(code.contains(#"setBody = JavaMethod("(Ljava/lang/String;)Lcom/example/fixture/Content/Builder;")"#))
    }

    func testEnumEmitsConstantsAsStaticFields() throws {
        let color = try node("com.example.fixture.Color")
        let code = render(color)
        XCTAssertTrue(code.contains("class Color(JavaClass, metaclass=MetaJavaClass):"))
        XCTAssertTrue(code.contains(#"__javaclass__ = "com/example/fixture/Color""#))
        XCTAssertTrue(code.contains(#"RED = JavaStaticField("Lcom/example/fixture/Color;")"#))
        XCTAssertTrue(code.contains(#"GREEN = JavaStaticField("Lcom/example/fixture/Color;")"#))
        XCTAssertTrue(code.contains(#"BLUE = JavaStaticField("Lcom/example/fixture/Color;")"#))
        XCTAssertTrue(code.contains(#"describe = JavaMethod("()Ljava/lang/String;")"#))
    }
}

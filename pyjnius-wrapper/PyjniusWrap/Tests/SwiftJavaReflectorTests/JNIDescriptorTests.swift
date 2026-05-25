import XCTest
@testable import SwiftJavaReflector

final class JNIDescriptorTests: XCTestCase {

    // MARK: - Primitive descriptors

    func testPrimitiveDescriptors() {
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "int"), "I")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "boolean"), "Z")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "byte"), "B")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "char"), "C")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "short"), "S")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "long"), "J")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "float"), "F")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "double"), "D")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "void"), "V")
    }

    // MARK: - Object descriptors

    func testObjectDescriptor() {
        XCTAssertEqual(
            JNIDescriptor.descriptor(forClassName: "java.lang.String"),
            "Ljava/lang/String;"
        )
        XCTAssertEqual(
            JNIDescriptor.descriptor(forClassName: "com.example.Foo"),
            "Lcom/example/Foo;"
        )
    }

    // MARK: - Array descriptors

    func testPrimitiveArrayDescriptor() {
        // Class.getName() for int[] returns "[I"
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "[I"), "[I")
        XCTAssertEqual(JNIDescriptor.descriptor(forClassName: "[[D"), "[[D")
    }

    func testObjectArrayDescriptor() {
        // Class.getName() for String[] returns "[Ljava.lang.String;"
        XCTAssertEqual(
            JNIDescriptor.descriptor(forClassName: "[Ljava.lang.String;"),
            "[Ljava/lang/String;"
        )
    }

    // MARK: - Method descriptors

    func testVoidNoArgs() {
        XCTAssertEqual(
            JNIDescriptor.methodDescriptor(paramTypeNames: [], returnTypeName: "void"),
            "()V"
        )
    }

    func testMethodWithParams() {
        XCTAssertEqual(
            JNIDescriptor.methodDescriptor(
                paramTypeNames: ["int", "java.lang.String"],
                returnTypeName: "void"
            ),
            "(ILjava/lang/String;)V"
        )
    }

    func testMethodWithObjectReturn() {
        XCTAssertEqual(
            JNIDescriptor.methodDescriptor(
                paramTypeNames: ["int"],
                returnTypeName: "java.lang.Object"
            ),
            "(I)Ljava/lang/Object;"
        )
    }

    func testMethodWithArrayParams() {
        XCTAssertEqual(
            JNIDescriptor.methodDescriptor(
                paramTypeNames: ["[I", "[Ljava.lang.String;"],
                returnTypeName: "boolean"
            ),
            "([I[Ljava/lang/String;)Z"
        )
    }

    // MARK: - JNI name conversion

    func testJniName() {
        XCTAssertEqual(JNIDescriptor.jniName(from: "com.example.Foo"), "com/example/Foo")
        XCTAssertEqual(JNIDescriptor.jniName(from: "java.lang.String"), "java/lang/String")
        XCTAssertEqual(JNIDescriptor.jniName(from: "Foo"), "Foo")
    }
}

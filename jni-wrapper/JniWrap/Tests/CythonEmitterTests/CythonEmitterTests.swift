import Foundation
import XCTest
@testable import CythonEmitter
@testable import JniWrapCore

/// Snapshot-style tests that pin the shape of the Cython emitter output.
/// Asserts strings we'd want to break the build on if they regress —
/// not a full byte-for-byte snapshot (intentional, so light formatting
/// tweaks don't churn the suite).
final class CythonEmitterTests: XCTestCase {

    private func loadPerson() throws -> AstDocument {
        let url = try XCTUnwrap(
            Bundle.module.url(forResource: "person.ast", withExtension: "json", subdirectory: "Fixtures")
        )
        return try JSONDecoder().decode(AstDocument.self, from: Data(contentsOf: url))
    }

    func testPyxContainsCoreShape() throws {
        let doc = try loadPerson()
        let cls = doc.classes.first { $0.simpleName == "Person" }!
        let pyx = CythonClassEmitter().renderPyx(cls)

        XCTAssertTrue(pyx.contains("# cython: language_level=3"))
        XCTAssertTrue(pyx.contains("from jni_core._core cimport ("))
        XCTAssertTrue(pyx.contains("from jni_core._dispatch cimport ("))
        XCTAssertTrue(pyx.contains("from jni_core.jni cimport ("))
        XCTAssertTrue(pyx.contains("include \"jni_core/conversions.pxi\""))

        XCTAssertTrue(pyx.contains("__javaclass__ = \"com/example/fixture/Person\""))
        XCTAssertTrue(pyx.contains("cdef jclass _cls_Person = NULL"))
        XCTAssertTrue(pyx.contains("cdef int _ensure_ids_Person(JNIEnv* env) except -1:"))
        XCTAssertTrue(pyx.contains("find_class_global(env, b\"com/example/fixture/Person\")"))

        XCTAssertTrue(pyx.contains("cdef class Person(JavaObject):"))
        XCTAssertTrue(pyx.contains("def __init__("))
        XCTAssertTrue(pyx.contains("jnicore_NewObjectA(env, _cls_Person,"))

        // Method IDs registered with their JNI sig
        XCTAssertTrue(pyx.contains("b\"<init>\", b\"(Ljava/lang/String;)V\""))
        XCTAssertTrue(pyx.contains("b\"getAge\", b\"()I\""))
        XCTAssertTrue(pyx.contains("get_static_method_id(env, _cls_Person, b\"anonymous\""))

        // Static field SPECIES — exposed as @staticmethod
        XCTAssertTrue(pyx.contains("get_static_field_id(env, _cls_Person, b\"SPECIES\""))

        // Overloaded greet — TODO marker present
        XCTAssertTrue(pyx.contains("# TODO:") && pyx.contains("overloads of greet"))
    }

    func testPxdDeclaresCdefClass() throws {
        let doc = try loadPerson()
        let cls = doc.classes.first { $0.simpleName == "Person" }!
        let pxd = CythonPxdEmitter().render(cls)
        XCTAssertTrue(pxd.contains("from jni_core._core cimport JavaObject"))
        XCTAssertTrue(pxd.contains("cdef class Person(JavaObject):"))
    }

    func testPipelineEmitWritesThreeFilesPerClass() throws {
        let doc = try loadPerson()
        let tmp = FileManager.default.temporaryDirectory
            .appendingPathComponent("cython-emitter-test-\(UUID().uuidString)")
        defer { try? FileManager.default.removeItem(at: tmp) }

        // Keep the package prefix so we exercise __init__.py emission
        // (Person's fqcn is com.example.fixture.Person → with stripping
        // turned off the pipeline creates a real package tree).
        let written = try CythonPipeline().emit(doc: doc, opts: .init(
            inputDir: tmp,
            outputDir: tmp,
            stripCommonPackagePrefix: false
        ))
        let pyxFiles = written.filter { $0.pathExtension == "pyx" }
        let pxdFiles = written.filter { $0.pathExtension == "pxd" }
        let pyiFiles = written.filter { $0.pathExtension == "pyi" }
        XCTAssertEqual(pyxFiles.count, doc.classes.count)
        XCTAssertEqual(pxdFiles.count, doc.classes.count)
        XCTAssertEqual(pyiFiles.count, doc.classes.count)
        XCTAssertTrue(written.contains { $0.lastPathComponent == "__init__.py" })

        // Sanity-check the Person file lives in the expected location and
        // contains a `cdef class` line for Person.
        let personPyx = pyxFiles.first { $0.lastPathComponent == "Person.pyx" }!
        let body = try String(contentsOf: personPyx, encoding: .utf8)
        XCTAssertTrue(body.contains("cdef class Person(JavaObject):"))
    }

    func testSingleFileLayoutFlattens() throws {
        let doc = try loadPerson()
        let tmp = FileManager.default.temporaryDirectory
            .appendingPathComponent("cython-emitter-flat-\(UUID().uuidString)")
        defer { try? FileManager.default.removeItem(at: tmp) }

        let written = try CythonPipeline().emit(doc: doc, opts: .init(
            inputDir: tmp,
            outputDir: tmp,
            singleFile: true
        ))
        let names = Set(written.map { $0.lastPathComponent })
        XCTAssertEqual(names, ["wrappers.pyx", "wrappers.pxd", "wrappers.pyi"])
    }
}

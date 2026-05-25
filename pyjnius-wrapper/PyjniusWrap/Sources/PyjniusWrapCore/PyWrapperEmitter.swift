import Foundation
import PySwiftAST
import PySwiftCodeGen

// Disambiguate from Foundation.Expression which Swift's stdlib pulls in.
private typealias Expr = PySwiftAST.Expression

/// Builds PySwiftAST `Module`s that produce pyjnius wrapper modules.
///
/// Emits a module per top-level class. Each class becomes:
/// ```python
/// from jnius import (
///     JavaClass, MetaJavaClass,
///     JavaMethod, JavaStaticMethod, JavaMultipleMethod,
///     JavaField, JavaStaticField,
/// )
///
/// __all__ = ["Person"]
///
/// class Person(JavaClass, metaclass=MetaJavaClass):
///     __javaclass__ = "com/example/fixture/Person"
///     __javaconstructor__ = [
///         ("(Ljava/lang/String;)V", False),
///         ("(Ljava/lang/String;I)V", False),
///     ]
///     SPECIES = JavaStaticField("Ljava/lang/String;")
///     name = JavaField("Ljava/lang/String;")
///     greet = JavaMultipleMethod([
///         ("(Ljava/lang/String;)Ljava/lang/String;", False, False),
///         ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False),
///     ])
///     anonymous = JavaStaticMethod("()Lcom/example/fixture/Person;")
///     getAge = JavaMethod("()I")
///     addTags = JavaMethod("([Ljava/lang/String;)V", varargs=True)
/// ```
public struct PyWrapperEmitter {

    public init() {}

    /// Convenience: build a module for the class and render it to Python source.
    public func render(_ cls: ClassNode) -> String {
        generatePythonCode(from: module(for: cls))
    }

    /// Build a top-level `Module` for the given class.
    public func module(for cls: ClassNode) -> Module {
        var body: [Statement] = []
        body.append(.importFrom(jniusImport()))
        body.append(.blank(.init(count: 1)))
        body.append(.assign(allAssign(names: [cls.simpleName])))
        body.append(.blank(.init(count: 1)))
        body.append(.classDef(classDef(for: cls)))
        return .module(body)
    }

    /// Build just the class definition (recursively for nested types).
    public func classDef(for cls: ClassNode) -> ClassDef {
        var classBody: [Statement] = []

        // __javaclass__
        classBody.append(.assign(.init(
            targets: [.name(Name(id: "__javaclass__"))],
            value: .constant(Constant(value: .string(cls.jniName))),
            typeComment: nil
        )))

        // __javaconstructor__ if class (not interface)
        if cls.kind == .classType && !cls.constructors.isEmpty {
            classBody.append(.assign(.init(
                targets: [.name(Name(id: "__javaconstructor__"))],
                value: .list(List(elts: cls.constructors.map(ctorTuple))),
                typeComment: nil
            )))
        }

        // Fields
        for field in cls.fields {
            classBody.append(.assign(.init(
                targets: [.name(Name(id: field.name))],
                value: fieldExpr(field),
                typeComment: nil
            )))
        }

        // Methods grouped by name → JavaMethod / JavaStaticMethod / JavaMultipleMethod
        let methodGroups = groupMethods(cls.methods)
        for (name, group) in methodGroups {
            classBody.append(.assign(.init(
                targets: [.name(Name(id: name))],
                value: methodExpr(name: name, methods: group),
                typeComment: nil
            )))
        }

        // Nested classes
        for nested in cls.nested {
            classBody.append(.blank(.init(count: 1)))
            classBody.append(.classDef(classDef(for: nested)))
        }

        // Enum constants surface as static-field stubs
        if cls.kind == .enumType, let constants = cls.enumConstants {
            for ec in constants {
                classBody.append(.assign(.init(
                    targets: [.name(Name(id: ec.name))],
                    value: .call(Call(
                        fun: .name(Name(id: "JavaStaticField")),
                        args: [.constant(Constant(value: .string("L" + cls.jniName + ";")))],
                        keywords: []
                    )),
                    typeComment: nil
                )))
            }
        }

        if classBody.isEmpty {
            classBody = [.pass(.init())]
        }

        // Bases differ for interfaces vs. classes
        let bases: [Expr]
        switch cls.kind {
        case .interfaceType:
            bases = [.name(Name(id: "JavaInterface"))]
        default:
            bases = [.name(Name(id: "JavaClass"))]
        }

        return ClassDef(
            name: cls.simpleName,
            bases: bases,
            keywords: [Keyword(arg: "metaclass", value: .name(Name(id: "MetaJavaClass")))],
            body: classBody
        )
    }

    // MARK: - Helpers

    private func jniusImport() -> ImportFrom {
        ImportFrom(
            module: "jnius",
            names: [
                Alias(name: "JavaClass",          asName: nil),
                Alias(name: "JavaInterface",      asName: nil),
                Alias(name: "MetaJavaClass",      asName: nil),
                Alias(name: "JavaMethod",         asName: nil),
                Alias(name: "JavaStaticMethod",   asName: nil),
                Alias(name: "JavaMultipleMethod", asName: nil),
                Alias(name: "JavaField",          asName: nil),
                Alias(name: "JavaStaticField",    asName: nil),
            ],
            level: 0
        )
    }

    private func allAssign(names: [String]) -> Assign {
        Assign(
            targets: [.name(Name(id: "__all__"))],
            value: .list(List(elts: names.map { .constant(Constant(value: .string($0))) })),
            typeComment: nil
        )
    }

    private func ctorTuple(_ c: ConstructorNode) -> Expr {
        .tuple(Tuple(elts: [
            .constant(Constant(value: .string(c.jniDescriptor))),
            .constant(Constant(value: .bool(c.isVarargs))),
        ]))
    }

    private func fieldExpr(_ f: FieldNode) -> Expr {
        let factory = f.isStatic ? "JavaStaticField" : "JavaField"
        return .call(Call(
            fun: .name(Name(id: factory)),
            args: [.constant(Constant(value: .string(f.jniDescriptor)))],
            keywords: []
        ))
    }

    /// Group by method name, preserving original order.
    private func groupMethods(_ methods: [MethodNode]) -> [(String, [MethodNode])] {
        var order: [String] = []
        var bucket: [String: [MethodNode]] = [:]
        for m in methods {
            if bucket[m.name] == nil { order.append(m.name) }
            bucket[m.name, default: []].append(m)
        }
        return order.map { ($0, bucket[$0]!) }
    }

    private func methodExpr(name: String, methods: [MethodNode]) -> Expr {
        if methods.count == 1 {
            let m = methods[0]
            let factory = m.isStatic ? "JavaStaticMethod" : "JavaMethod"
            var kwargs: [Keyword] = []
            if m.isVarargs {
                kwargs.append(Keyword(arg: "varargs", value: .constant(Constant(value: .bool(true)))))
            }
            return .call(Call(
                fun: .name(Name(id: factory)),
                args: [.constant(Constant(value: .string(m.jniDescriptor)))],
                keywords: kwargs
            ))
        }
        // JavaMultipleMethod([(sig, is_static, is_varargs), ...])
        let entries: [Expr] = methods.map { m in
            .tuple(Tuple(elts: [
                .constant(Constant(value: .string(m.jniDescriptor))),
                .constant(Constant(value: .bool(m.isStatic))),
                .constant(Constant(value: .bool(m.isVarargs))),
            ]))
        }
        return .call(Call(
            fun: .name(Name(id: "JavaMultipleMethod")),
            args: [.list(List(elts: entries))],
            keywords: []
        ))
    }
}

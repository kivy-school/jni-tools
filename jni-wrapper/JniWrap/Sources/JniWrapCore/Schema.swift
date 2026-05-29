import Foundation

/// Schema definitions for the AST representation of Java classes.
///
/// These types represent the intermediate data model produced by the
/// `SwiftJavaReflector` (via embedded JVM reflection or JavaParser)
/// and consumed by the Python code generation pipeline.
public struct AstDocument: Codable, Sendable {
    public let classes: [ClassNode]

    public init(classes: [ClassNode]) {
        self.classes = classes
    }
}

public enum ClassKind: String, Codable, Sendable {
    case classType = "CLASS"
    case interfaceType = "INTERFACE"
    case enumType = "ENUM"
    case annotationType = "ANNOTATION"
}

public enum JavaModifier: String, Codable, Sendable {
    case `public`  = "PUBLIC"
    case `protected` = "PROTECTED"
    case `private` = "PRIVATE"
    case `static`  = "STATIC"
    case `final`   = "FINAL"
    case abstract  = "ABSTRACT"
    case `default` = "DEFAULT"
}

public struct ClassNode: Codable, Sendable {
    public let fqcn: String
    public let jniName: String
    public let simpleName: String
    public let kind: ClassKind

    /// Cython-safe identifier for use within a single .pyx file.
    ///
    /// For singly-nested classes (e.g. `Outer$Builder`) this equals
    /// `simpleName` (`Builder`).  For doubly- or multiply-nested classes
    /// (e.g. `Outer$Inner$Builder`) the outermost class name is dropped and
    /// the remaining components are joined with `_` → `Inner_Builder`.  This
    /// prevents collisions when multiple nested builders end up in one file.
    public var cythonLocalName: String {
        // jniName = "pkg/Outer$Inner$Leaf" (slashes, dollar signs)
        let lastSlash = jniName.split(separator: "/").last.map(String.init) ?? simpleName
        let parts = lastSlash.split(separator: "$").map(String.init)
        guard parts.count >= 3 else { return simpleName }
        // Drop outermost class name; join the rest with "_"
        return parts.dropFirst().joined(separator: "_")
    }
    public let modifiers: [JavaModifier]
    public let superclass: String?
    public let interfaces: [String]
    public let javadoc: String?
    public let fields: [FieldNode]
    public let constructors: [ConstructorNode]
    public let methods: [MethodNode]
    public let nested: [ClassNode]
    public let enumConstants: [EnumConstantNode]?

    public init(fqcn: String, jniName: String, simpleName: String, kind: ClassKind,
                modifiers: [JavaModifier], superclass: String?, interfaces: [String],
                javadoc: String?, fields: [FieldNode], constructors: [ConstructorNode],
                methods: [MethodNode], nested: [ClassNode], enumConstants: [EnumConstantNode]?) {
        self.fqcn = fqcn
        self.jniName = jniName
        self.simpleName = simpleName
        self.kind = kind
        self.modifiers = modifiers
        self.superclass = superclass
        self.interfaces = interfaces
        self.javadoc = javadoc
        self.fields = fields
        self.constructors = constructors
        self.methods = methods
        self.nested = nested
        self.enumConstants = enumConstants
    }
}

public struct FieldNode: Codable, Sendable {
    public let name: String
    public let jniDescriptor: String
    public let typeFqcn: String
    public let isStatic: Bool
    public let modifiers: [JavaModifier]
    public let javadoc: String?

    public init(name: String, jniDescriptor: String, typeFqcn: String,
                isStatic: Bool, modifiers: [JavaModifier], javadoc: String?) {
        self.name = name
        self.jniDescriptor = jniDescriptor
        self.typeFqcn = typeFqcn
        self.isStatic = isStatic
        self.modifiers = modifiers
        self.javadoc = javadoc
    }
}

public struct ParamNode: Codable, Sendable {
    public let name: String
    public let jniDescriptor: String
    public let typeFqcn: String

    public init(name: String, jniDescriptor: String, typeFqcn: String) {
        self.name = name
        self.jniDescriptor = jniDescriptor
        self.typeFqcn = typeFqcn
    }
}

public struct ConstructorNode: Codable, Sendable {
    public let jniDescriptor: String
    public let isVarargs: Bool
    public let modifiers: [JavaModifier]
    public let parameters: [ParamNode]
    public let javadoc: String?

    public init(jniDescriptor: String, isVarargs: Bool, modifiers: [JavaModifier],
                parameters: [ParamNode], javadoc: String?) {
        self.jniDescriptor = jniDescriptor
        self.isVarargs = isVarargs
        self.modifiers = modifiers
        self.parameters = parameters
        self.javadoc = javadoc
    }
}

public struct MethodNode: Codable, Sendable {
    public let name: String
    public let jniDescriptor: String
    public let isStatic: Bool
    public let isVarargs: Bool
    public let modifiers: [JavaModifier]
    public let parameters: [ParamNode]
    public let returnTypeFqcn: String
    public let javadoc: String?

    public init(name: String, jniDescriptor: String, isStatic: Bool, isVarargs: Bool,
                modifiers: [JavaModifier], parameters: [ParamNode],
                returnTypeFqcn: String, javadoc: String?) {
        self.name = name
        self.jniDescriptor = jniDescriptor
        self.isStatic = isStatic
        self.isVarargs = isVarargs
        self.modifiers = modifiers
        self.parameters = parameters
        self.returnTypeFqcn = returnTypeFqcn
        self.javadoc = javadoc
    }
}

public struct EnumConstantNode: Codable, Sendable {
    public let name: String
    public let javadoc: String?

    public init(name: String, javadoc: String?) {
        self.name = name
        self.javadoc = javadoc
    }
}

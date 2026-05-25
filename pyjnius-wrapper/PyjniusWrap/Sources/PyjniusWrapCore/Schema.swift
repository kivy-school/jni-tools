import Foundation

/// Codable mirror of the JSON produced by `java-ast-emitter.jar`.
///
/// Keep field names in sync with the Java DTOs in
/// `pyjnius-wrapper/java-ast-emitter/src/main/java/dev/kivyschool/pyjniuswrap/AstDtos.java`.
public struct AstDocument: Codable, Sendable {
    public let classes: [ClassNode]
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
    public let modifiers: [JavaModifier]
    public let superclass: String?
    public let interfaces: [String]
    public let javadoc: String?
    public let fields: [FieldNode]
    public let constructors: [ConstructorNode]
    public let methods: [MethodNode]
    public let nested: [ClassNode]
    public let enumConstants: [EnumConstantNode]?
}

public struct FieldNode: Codable, Sendable {
    public let name: String
    public let jniDescriptor: String
    public let typeFqcn: String
    public let isStatic: Bool
    public let modifiers: [JavaModifier]
    public let javadoc: String?
}

public struct ParamNode: Codable, Sendable {
    public let name: String
    public let jniDescriptor: String
    public let typeFqcn: String
}

public struct ConstructorNode: Codable, Sendable {
    public let jniDescriptor: String
    public let isVarargs: Bool
    public let modifiers: [JavaModifier]
    public let parameters: [ParamNode]
    public let javadoc: String?
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
}

public struct EnumConstantNode: Codable, Sendable {
    public let name: String
    public let javadoc: String?
}

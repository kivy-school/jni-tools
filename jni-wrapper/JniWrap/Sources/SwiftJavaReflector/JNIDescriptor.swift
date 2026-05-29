import Foundation

/// Converts `java.lang.Class.getName()` strings to JNI descriptor strings.
///
/// Examples:
/// - `int` → `"I"`
/// - `java.lang.String` → `"Ljava/lang/String;"`
/// - `[I` → `"[I"`
/// - `[Ljava.lang.String;` → `"[Ljava/lang/String;"`
public enum JNIDescriptor {

    /// Primitive type name → JNI descriptor character mapping.
    private static let primitiveMap: [String: String] = [
        "void":    "V",
        "boolean": "Z",
        "byte":    "B",
        "char":    "C",
        "short":   "S",
        "int":     "I",
        "long":    "J",
        "float":   "F",
        "double":  "D",
    ]

    /// Returns the JNI type descriptor for the given `Class.getName()` string.
    ///
    /// - Primitives: `"int"`, `"boolean"`, etc.
    /// - Object types: `"java.lang.String"`, `"com.example.Foo"`
    /// - Array types: `"[I"`, `"[Ljava.lang.String;"`, `"[[D"`
    public static func descriptor(forClassName className: String) -> String {
        if let prim = primitiveMap[className] {
            return prim
        }
        // Array types are already in JNI form except for `.`→`/` in object refs.
        if className.hasPrefix("[") {
            return className.replacingOccurrences(of: ".", with: "/")
        }
        // Object types: wrap in L...;
        return "L\(className.replacingOccurrences(of: ".", with: "/"));"
    }

    /// Builds a full JNI method descriptor from parameter and return type names.
    ///
    /// Example: `(["int", "java.lang.String"], "void")` → `"(ILjava/lang/String;)V"`
    public static func methodDescriptor(paramTypeNames: [String],
                                        returnTypeName: String) -> String {
        let params = paramTypeNames.map { descriptor(forClassName: $0) }.joined()
        let ret = descriptor(forClassName: returnTypeName)
        return "(\(params))\(ret)"
    }

    /// Converts a fully-qualified class name to JNI internal name.
    /// Example: `"com.example.Foo"` → `"com/example/Foo"`.
    public static func jniName(from fqcn: String) -> String {
        fqcn.replacingOccurrences(of: ".", with: "/")
    }
}

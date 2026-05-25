import Foundation
import PyjniusWrapCore
import SwiftJava
import JavaLangReflect

/// Converts `java.lang.Class` objects to JNI descriptor strings.
///
/// Examples:
/// - `int` → `"I"`
/// - `java.lang.String` → `"Ljava/lang/String;"`
/// - `int[]` → `"[I"`
/// - `java.lang.String[]` → `"[Ljava/lang/String;"`
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

    /// Returns the JNI type descriptor for a given `java.lang.Class` name.
    ///
    /// The `className` should be the result of `Class.getName()`:
    /// - Primitives: `"int"`, `"boolean"`, etc.
    /// - Object types: `"java.lang.String"`, `"com.example.Foo"`
    /// - Array types: `"[I"`, `"[Ljava.lang.String;"`, `"[[D"`
    public static func descriptor(forClassName className: String) -> String {
        // Primitive types
        if let prim = primitiveMap[className] {
            return prim
        }

        // Array types: Class.getName() returns "[I", "[Ljava.lang.String;", etc.
        // Already in JNI format but with dots instead of slashes in object refs.
        if className.hasPrefix("[") {
            return className.replacingOccurrences(of: ".", with: "/")
        }

        // Object types: wrap in L...;
        return "L\(className.replacingOccurrences(of: ".", with: "/"));"
    }

    /// Builds a full JNI method descriptor from parameter type names and return type name.
    ///
    /// Example: `(["int", "java.lang.String"], "void")` → `"(ILjava/lang/String;)V"`
    public static func methodDescriptor(paramTypeNames: [String], returnTypeName: String) -> String {
        let params = paramTypeNames.map { descriptor(forClassName: $0) }.joined()
        let ret = descriptor(forClassName: returnTypeName)
        return "(\(params))\(ret)"
    }

    /// Converts a fully-qualified class name (dot-separated) to JNI internal name (slash-separated).
    ///
    /// Example: `"com.example.Foo"` → `"com/example/Foo"`
    public static func jniName(from fqcn: String) -> String {
        fqcn.replacingOccurrences(of: ".", with: "/")
    }
}

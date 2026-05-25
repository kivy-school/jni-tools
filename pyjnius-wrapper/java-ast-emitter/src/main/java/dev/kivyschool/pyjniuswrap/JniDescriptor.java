package dev.kivyschool.pyjniuswrap;

import com.github.javaparser.ast.type.ArrayType;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.PrimitiveType;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.type.VoidType;
import com.github.javaparser.resolution.UnsolvedSymbolException;
import com.github.javaparser.resolution.types.ResolvedArrayType;
import com.github.javaparser.resolution.types.ResolvedPrimitiveType;
import com.github.javaparser.resolution.types.ResolvedReferenceType;
import com.github.javaparser.resolution.types.ResolvedType;
import com.github.javaparser.resolution.types.ResolvedVoidType;

/**
 * Builds JNI type descriptors (e.g. {@code Ljava/lang/String;}, {@code [I}, {@code (II)V}).
 *
 * <p>Uses JavaParser's symbol solver when available; falls back to a heuristic that
 * preserves the source's written type when resolution fails (e.g. types from an SDK
 * jar that's not on the classpath).
 */
public final class JniDescriptor {

    private JniDescriptor() {}

    /** JNI descriptor for a parser AST Type, with symbol-solver assist. */
    public static String of(Type type) {
        if (type instanceof VoidType) {
            return "V";
        }
        if (type instanceof PrimitiveType) {
            return primitive(((PrimitiveType) type).getType());
        }
        if (type instanceof ArrayType) {
            return "[" + of(((ArrayType) type).getComponentType());
        }
        // Try symbol-solver resolution first for fully-qualified output.
        try {
            ResolvedType resolved = type.resolve();
            return ofResolved(resolved);
        } catch (RuntimeException e) {
            // Fall back to the textual class name. Treat as java.lang.<Name> if not dotted.
            if (type instanceof ClassOrInterfaceType) {
                ClassOrInterfaceType ct = (ClassOrInterfaceType) type;
                String name = ct.getNameWithScope();
                return "L" + fqcnFallback(name).replace('.', '/') + ";";
            }
            // Last resort: java.lang.Object
            return "Ljava/lang/Object;";
        }
    }

    /** JNI descriptor for a resolved type. */
    public static String ofResolved(ResolvedType resolved) {
        if (resolved.isVoid() || resolved instanceof ResolvedVoidType) {
            return "V";
        }
        if (resolved.isPrimitive()) {
            return primitiveOf(resolved.asPrimitive());
        }
        if (resolved.isArray()) {
            return "[" + ofResolved(((ResolvedArrayType) resolved).getComponentType());
        }
        if (resolved.isReferenceType()) {
            ResolvedReferenceType ref = resolved.asReferenceType();
            return "L" + ref.getQualifiedName().replace('.', '/') + ";";
        }
        if (resolved.isTypeVariable()) {
            // Generic erasure → java.lang.Object (or bound if available).
            return "Ljava/lang/Object;";
        }
        return "Ljava/lang/Object;";
    }

    /** FQCN best-effort for a resolved or AST type. */
    public static String fqcnOf(Type type) {
        if (type instanceof VoidType) return "void";
        if (type instanceof PrimitiveType) return ((PrimitiveType) type).getType().asString();
        if (type instanceof ArrayType) return fqcnOf(((ArrayType) type).getComponentType()) + "[]";
        try {
            ResolvedType resolved = type.resolve();
            return fqcnOfResolved(resolved);
        } catch (RuntimeException e) {
            if (type instanceof ClassOrInterfaceType) {
                return fqcnFallback(((ClassOrInterfaceType) type).getNameWithScope());
            }
            return "java.lang.Object";
        }
    }

    public static String fqcnOfResolved(ResolvedType resolved) {
        if (resolved.isVoid()) return "void";
        if (resolved.isPrimitive()) return resolved.asPrimitive().describe();
        if (resolved.isArray()) {
            return fqcnOfResolved(((ResolvedArrayType) resolved).getComponentType()) + "[]";
        }
        if (resolved.isReferenceType()) {
            return resolved.asReferenceType().getQualifiedName();
        }
        return "java.lang.Object";
    }

    private static String primitive(PrimitiveType.Primitive p) {
        switch (p) {
            case BOOLEAN: return "Z";
            case BYTE:    return "B";
            case CHAR:    return "C";
            case SHORT:   return "S";
            case INT:     return "I";
            case LONG:    return "J";
            case FLOAT:   return "F";
            case DOUBLE:  return "D";
            default:      throw new IllegalArgumentException("Unknown primitive: " + p);
        }
    }

    private static String primitiveOf(ResolvedPrimitiveType prim) {
        switch (prim) {
            case BOOLEAN: return "Z";
            case BYTE:    return "B";
            case CHAR:    return "C";
            case SHORT:   return "S";
            case INT:     return "I";
            case LONG:    return "J";
            case FLOAT:   return "F";
            case DOUBLE:  return "D";
            default: throw new IllegalArgumentException("Unknown primitive: " + prim);
        }
    }

    private static String fqcnFallback(String written) {
        if (written.contains(".")) return written;
        // Common java.lang shortcuts so unresolved imports don't poison the descriptor.
        switch (written) {
            case "String": case "Object": case "Integer": case "Long":
            case "Short": case "Byte": case "Float": case "Double":
            case "Boolean": case "Character": case "Number":
            case "CharSequence": case "Throwable": case "Exception":
            case "RuntimeException": case "Class": case "Iterable":
                return "java.lang." + written;
            default:
                // Unknown — assume the writer meant a type in the same package.
                // Caller should override via imports if possible.
                return written;
        }
    }
}

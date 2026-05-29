from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HexFormat"]

class HexFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/HexFormat"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isUpperCase = JavaMethod("()Z")
    of = JavaStaticMethod("()Ljava/util/HexFormat;")
    prefix = JavaMethod("()Ljava/lang/String;")
    suffix = JavaMethod("()Ljava/lang/String;")
    delimiter = JavaMethod("()Ljava/lang/String;")
    withUpperCase = JavaMethod("()Ljava/util/HexFormat;")
    toHexDigits = JavaMultipleMethod([("(JI)Ljava/lang/String;", False, False), ("(J)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False), ("(C)Ljava/lang/String;", False, False), ("(S)Ljava/lang/String;", False, False), ("(B)Ljava/lang/String;", False, False), ("(Ljava/lang/Appendable;B)Ljava/lang/Appendable;", False, False)])
    formatHex = JavaMultipleMethod([("(Ljava/lang/Appendable;[B)Ljava/lang/Appendable;", False, False), ("([BII)Ljava/lang/String;", False, False), ("([B)Ljava/lang/String;", False, False), ("(Ljava/lang/Appendable;[BII)Ljava/lang/Appendable;", False, False)])
    parseHex = JavaMultipleMethod([("(Ljava/lang/CharSequence;)[B", False, False), ("([CII)[B", False, False), ("(Ljava/lang/CharSequence;II)[B", False, False)])
    fromHexDigits = JavaMultipleMethod([("(Ljava/lang/CharSequence;)I", True, False), ("(Ljava/lang/CharSequence;II)I", True, False)])
    toHighHexDigit = JavaMethod("(I)C")
    toLowHexDigit = JavaMethod("(I)C")
    fromHexDigit = JavaStaticMethod("(I)I")
    fromHexDigitsToLong = JavaMultipleMethod([("(Ljava/lang/CharSequence;II)J", True, False), ("(Ljava/lang/CharSequence;)J", True, False)])
    ofDelimiter = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withDelimiter = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withPrefix = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withSuffix = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withLowerCase = JavaMethod("()Ljava/util/HexFormat;")
    isHexDigit = JavaStaticMethod("(I)Z")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HexFormat"]

class HexFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/HexFormat"
    of = JavaStaticMethod("()Ljava/util/HexFormat;")
    ofDelimiter = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withDelimiter = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withPrefix = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withSuffix = JavaMethod("(Ljava/lang/String;)Ljava/util/HexFormat;")
    withUpperCase = JavaMethod("()Ljava/util/HexFormat;")
    withLowerCase = JavaMethod("()Ljava/util/HexFormat;")
    delimiter = JavaMethod("()Ljava/lang/String;")
    prefix = JavaMethod("()Ljava/lang/String;")
    suffix = JavaMethod("()Ljava/lang/String;")
    isUpperCase = JavaMethod("()Z")
    formatHex = JavaMultipleMethod([("([B)Ljava/lang/String;", False, False), ("([BII)Ljava/lang/String;", False, False), ("(Ljava/lang/Appendable;[B)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/Appendable;[BII)Ljava/lang/Appendable;", False, False)])
    parseHex = JavaMultipleMethod([("(Ljava/lang/CharSequence;)[B", False, False), ("(Ljava/lang/CharSequence;II)[B", False, False), ("([CII)[B", False, False)])
    toLowHexDigit = JavaMethod("(I)C")
    toHighHexDigit = JavaMethod("(I)C")
    toHexDigits = JavaMultipleMethod([("(Ljava/lang/Appendable;B)Ljava/lang/Appendable;", False, False), ("(B)Ljava/lang/String;", False, False), ("(C)Ljava/lang/String;", False, False), ("(S)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False), ("(J)Ljava/lang/String;", False, False), ("(JI)Ljava/lang/String;", False, False)])
    isHexDigit = JavaStaticMethod("(I)Z")
    fromHexDigit = JavaStaticMethod("(I)I")
    fromHexDigits = JavaMultipleMethod([("(Ljava/lang/CharSequence;)I", True, False), ("(Ljava/lang/CharSequence;II)I", True, False)])
    fromHexDigitsToLong = JavaMultipleMethod([("(Ljava/lang/CharSequence;)J", True, False), ("(Ljava/lang/CharSequence;II)J", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
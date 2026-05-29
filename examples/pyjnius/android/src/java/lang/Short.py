from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Short"]

class Short(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Short"
    __javaconstructor__ = [("(S)V", False), ("(Ljava/lang/String;)V", False)]
    BYTES = JavaStaticField("I")
    MAX_VALUE = JavaStaticField("S")
    MIN_VALUE = JavaStaticField("S")
    SIZE = JavaStaticField("I")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    toString = JavaMultipleMethod([("(S)Ljava/lang/String;", True, False), ("()Ljava/lang/String;", False, False)])
    parseShort = JavaMultipleMethod([("(Ljava/lang/String;I)S", True, False), ("(Ljava/lang/String;)S", True, False)])
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;I)Ljava/lang/Short;", True, False), ("(Ljava/lang/String;)Ljava/lang/Short;", True, False), ("(S)Ljava/lang/Short;", True, False)])
    decode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Short;")
    byteValue = JavaMethod("()B")
    shortValue = JavaMethod("()S")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    hashCode = JavaMultipleMethod([("()I", False, False), ("(S)I", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/lang/Short;)I")
    compare = JavaStaticMethod("(SS)I")
    compareUnsigned = JavaStaticMethod("(SS)I")
    reverseBytes = JavaStaticMethod("(S)S")
    toUnsignedInt = JavaStaticMethod("(S)I")
    toUnsignedLong = JavaStaticMethod("(S)J")
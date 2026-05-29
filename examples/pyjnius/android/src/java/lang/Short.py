from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Short"]

class Short(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Short"
    __javaconstructor__ = [("(S)V", False), ("(Ljava/lang/String;)V", False)]
    MIN_VALUE = JavaStaticField("S")
    MAX_VALUE = JavaStaticField("S")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    SIZE = JavaStaticField("I")
    BYTES = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(S)Ljava/lang/String;", True, False)])
    hashCode = JavaMultipleMethod([("(S)I", True, False), ("()I", False, False)])
    compareUnsigned = JavaStaticMethod("(SS)I")
    reverseBytes = JavaStaticMethod("(S)S")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Short;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    compare = JavaStaticMethod("(SS)I")
    byteValue = JavaMethod("()B")
    shortValue = JavaMethod("()S")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;I)Ljava/lang/Short;", True, False), ("(Ljava/lang/String;)Ljava/lang/Short;", True, False), ("(S)Ljava/lang/Short;", True, False)])
    decode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Short;")
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    toUnsignedLong = JavaStaticMethod("(S)J")
    toUnsignedInt = JavaStaticMethod("(S)I")
    parseShort = JavaMultipleMethod([("(Ljava/lang/String;)S", True, False), ("(Ljava/lang/String;I)S", True, False)])
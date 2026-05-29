from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Byte"]

class Byte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Byte"
    __javaconstructor__ = [("(B)V", False), ("(Ljava/lang/String;)V", False)]
    MIN_VALUE = JavaStaticField("B")
    MAX_VALUE = JavaStaticField("B")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    SIZE = JavaStaticField("I")
    BYTES = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(B)Ljava/lang/String;", True, False)])
    hashCode = JavaMultipleMethod([("(B)I", True, False), ("()I", False, False)])
    compareUnsigned = JavaStaticMethod("(BB)I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Byte;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    compare = JavaStaticMethod("(BB)I")
    byteValue = JavaMethod("()B")
    shortValue = JavaMethod("()S")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Byte;", True, False), ("(Ljava/lang/String;I)Ljava/lang/Byte;", True, False), ("(B)Ljava/lang/Byte;", True, False)])
    decode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Byte;")
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    toUnsignedLong = JavaStaticMethod("(B)J")
    toUnsignedInt = JavaStaticMethod("(B)I")
    parseByte = JavaMultipleMethod([("(Ljava/lang/String;)B", True, False), ("(Ljava/lang/String;I)B", True, False)])
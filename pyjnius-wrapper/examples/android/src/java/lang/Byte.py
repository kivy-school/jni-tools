from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Byte"]

class Byte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Byte"
    __javaconstructor__ = [("(B)V", False), ("(Ljava/lang/String;)V", False)]
    BYTES = JavaStaticField("I")
    MAX_VALUE = JavaStaticField("B")
    MIN_VALUE = JavaStaticField("B")
    SIZE = JavaStaticField("I")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    toString = JavaMultipleMethod([("(B)Ljava/lang/String;", True, False), ("()Ljava/lang/String;", False, False)])
    valueOf = JavaMultipleMethod([("(B)Ljava/lang/Byte;", True, False), ("(Ljava/lang/String;I)Ljava/lang/Byte;", True, False), ("(Ljava/lang/String;)Ljava/lang/Byte;", True, False)])
    parseByte = JavaMultipleMethod([("(Ljava/lang/String;I)B", True, False), ("(Ljava/lang/String;)B", True, False)])
    decode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Byte;")
    byteValue = JavaMethod("()B")
    shortValue = JavaMethod("()S")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    hashCode = JavaMultipleMethod([("()I", False, False), ("(B)I", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/lang/Byte;)I")
    compare = JavaStaticMethod("(BB)I")
    compareUnsigned = JavaStaticMethod("(BB)I")
    toUnsignedInt = JavaStaticMethod("(B)I")
    toUnsignedLong = JavaStaticMethod("(B)J")
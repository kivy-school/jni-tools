from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UUID"]

class UUID(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/UUID"
    __javaconstructor__ = [("(JJ)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    version = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/util/UUID;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    timestamp = JavaMethod("()J")
    variant = JavaMethod("()I")
    randomUUID = JavaStaticMethod("()Ljava/util/UUID;")
    nameUUIDFromBytes = JavaStaticMethod("([B)Ljava/util/UUID;")
    ofEpochMillis = JavaStaticMethod("(J)Ljava/util/UUID;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/UUID;")
    getLeastSignificantBits = JavaMethod("()J")
    getMostSignificantBits = JavaMethod("()J")
    clockSequence = JavaMethod("()I")
    node = JavaMethod("()J")
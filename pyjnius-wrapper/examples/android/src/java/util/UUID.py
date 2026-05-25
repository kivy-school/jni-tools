from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UUID"]

class UUID(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/UUID"
    __javaconstructor__ = [("(JJ)V", False)]
    randomUUID = JavaStaticMethod("()Ljava/util/UUID;")
    nameUUIDFromBytes = JavaStaticMethod("([B)Ljava/util/UUID;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/UUID;")
    getLeastSignificantBits = JavaMethod("()J")
    getMostSignificantBits = JavaMethod("()J")
    version = JavaMethod("()I")
    variant = JavaMethod("()I")
    timestamp = JavaMethod("()J")
    clockSequence = JavaMethod("()I")
    node = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/util/UUID;)I")
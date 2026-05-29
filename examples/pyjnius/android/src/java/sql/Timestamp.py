from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timestamp"]

class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Timestamp"
    __javaconstructor__ = [("(IIIIIII)V", False), ("(J)V", False)]
    getNanos = JavaMethod("()I")
    setNanos = JavaMethod("(I)V")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/sql/Timestamp;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/util/Date;)I", False, False), ("(Ljava/sql/Timestamp;)I", False, False)])
    valueOf = JavaMultipleMethod([("(Ljava/time/LocalDateTime;)Ljava/sql/Timestamp;", True, False), ("(Ljava/lang/String;)Ljava/sql/Timestamp;", True, False)])
    from = JavaStaticMethod("(Ljava/time/Instant;)Ljava/sql/Timestamp;")
    before = JavaMethod("(Ljava/sql/Timestamp;)Z")
    after = JavaMethod("(Ljava/sql/Timestamp;)Z")
    toLocalDateTime = JavaMethod("()Ljava/time/LocalDateTime;")
    getTime = JavaMethod("()J")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    setTime = JavaMethod("(J)V")
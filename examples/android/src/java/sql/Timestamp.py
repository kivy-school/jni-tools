from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timestamp"]

class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Timestamp"
    __javaconstructor__ = [("(IIIIIII)V", False), ("(J)V", False)]
    setTime = JavaMethod("(J)V")
    getTime = JavaMethod("()J")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/Timestamp;")
    toString = JavaMethod("()Ljava/lang/String;")
    getNanos = JavaMethod("()I")
    setNanos = JavaMethod("(I)V")
    equals = JavaMultipleMethod([("(Ljava/sql/Timestamp;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    before = JavaMethod("(Ljava/sql/Timestamp;)Z")
    after = JavaMethod("(Ljava/sql/Timestamp;)Z")
    compareTo = JavaMultipleMethod([("(Ljava/sql/Timestamp;)I", False, False), ("(Ljava/util/Date;)I", False, False)])
    hashCode = JavaMethod("()I")
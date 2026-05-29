from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Date"]

class Date(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Date"
    __javaconstructor__ = [("(III)V", False), ("(J)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/sql/Date;", True, False), ("(Ljava/time/LocalDate;)Ljava/sql/Date;", True, False)])
    toLocalDate = JavaMethod("()Ljava/time/LocalDate;")
    getHours = JavaMethod("()I")
    setHours = JavaMethod("(I)V")
    getMinutes = JavaMethod("()I")
    setMinutes = JavaMethod("(I)V")
    setSeconds = JavaMethod("(I)V")
    getSeconds = JavaMethod("()I")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    setTime = JavaMethod("(J)V")
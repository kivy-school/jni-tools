from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Time"]

class Time(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Time"
    __javaconstructor__ = [("(III)V", False), ("(J)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/sql/Time;", True, False), ("(Ljava/time/LocalTime;)Ljava/sql/Time;", True, False)])
    getMonth = JavaMethod("()I")
    getDate = JavaMethod("()I")
    setDate = JavaMethod("(I)V")
    setMonth = JavaMethod("(I)V")
    setYear = JavaMethod("(I)V")
    getDay = JavaMethod("()I")
    toLocalTime = JavaMethod("()Ljava/time/LocalTime;")
    getYear = JavaMethod("()I")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    setTime = JavaMethod("(J)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Time"]

class Time(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Time"
    __javaconstructor__ = [("(III)V", False), ("(J)V", False)]
    setTime = JavaMethod("(J)V")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/Time;")
    toString = JavaMethod("()Ljava/lang/String;")
    getYear = JavaMethod("()I")
    getMonth = JavaMethod("()I")
    getDay = JavaMethod("()I")
    getDate = JavaMethod("()I")
    setYear = JavaMethod("(I)V")
    setMonth = JavaMethod("(I)V")
    setDate = JavaMethod("(I)V")
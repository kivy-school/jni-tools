from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Date"]

class Date(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Date"
    __javaconstructor__ = [("(III)V", False), ("(J)V", False)]
    setTime = JavaMethod("(J)V")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/Date;")
    toString = JavaMethod("()Ljava/lang/String;")
    getHours = JavaMethod("()I")
    getMinutes = JavaMethod("()I")
    getSeconds = JavaMethod("()I")
    setHours = JavaMethod("(I)V")
    setMinutes = JavaMethod("(I)V")
    setSeconds = JavaMethod("(I)V")
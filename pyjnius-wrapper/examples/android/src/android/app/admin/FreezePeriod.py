from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FreezePeriod"]

class FreezePeriod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/FreezePeriod"
    __javaconstructor__ = [("(Ljava/time/MonthDay;Ljava/time/MonthDay;)V", False)]
    getStart = JavaMethod("()Ljava/time/MonthDay;")
    getEnd = JavaMethod("()Ljava/time/MonthDay;")
    toString = JavaMethod("()Ljava/lang/String;")
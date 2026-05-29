from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FreezePeriod"]

class FreezePeriod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/FreezePeriod"
    __javaconstructor__ = [("(Ljava/time/MonthDay;Ljava/time/MonthDay;)V", False)]
    getEnd = JavaMethod("()Ljava/time/MonthDay;")
    getStart = JavaMethod("()Ljava/time/MonthDay;")
    toString = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateInterval"]

class DateInterval(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/DateInterval"
    __javaconstructor__ = [("(JJ)V", False)]
    getFromDate = JavaMethod("()J")
    getToDate = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
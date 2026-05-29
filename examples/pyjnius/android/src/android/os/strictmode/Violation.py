from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Violation"]

class Violation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/Violation"
    fillInStackTrace = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    hashCode = JavaMethod("()I")
    setStackTrace = JavaMethod("([Ljava/lang/StackTraceElement;)V")
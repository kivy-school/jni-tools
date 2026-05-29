from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Violation"]

class Violation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/Violation"
    hashCode = JavaMethod("()I")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    setStackTrace = JavaMethod("([Ljava/lang/StackTraceElement;)V")
    fillInStackTrace = JavaMethod("()Ljava/lang/Throwable;")
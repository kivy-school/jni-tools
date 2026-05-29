from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Trace"]

class Trace(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Trace"
    isEnabled = JavaStaticMethod("()Z")
    endSection = JavaStaticMethod("()V")
    setCounter = JavaStaticMethod("(Ljava/lang/String;J)V")
    beginSection = JavaStaticMethod("(Ljava/lang/String;)V")
    beginAsyncSection = JavaStaticMethod("(Ljava/lang/String;I)V")
    endAsyncSection = JavaStaticMethod("(Ljava/lang/String;I)V")
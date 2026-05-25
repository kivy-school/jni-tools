from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Trace"]

class Trace(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Trace"
    isEnabled = JavaStaticMethod("()Z")
    beginSection = JavaStaticMethod("(Ljava/lang/String;)V")
    endSection = JavaStaticMethod("()V")
    beginAsyncSection = JavaStaticMethod("(Ljava/lang/String;I)V")
    endAsyncSection = JavaStaticMethod("(Ljava/lang/String;I)V")
    setCounter = JavaStaticMethod("(Ljava/lang/String;J)V")
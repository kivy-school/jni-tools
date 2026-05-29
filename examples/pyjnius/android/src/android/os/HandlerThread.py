from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandlerThread"]

class HandlerThread(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/HandlerThread"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    MIN_PRIORITY = JavaStaticField("I")
    NORM_PRIORITY = JavaStaticField("I")
    MAX_PRIORITY = JavaStaticField("I")
    quit = JavaMethod("()Z")
    quitSafely = JavaMethod("()Z")
    run = JavaMethod("()V")
    getLooper = JavaMethod("()Landroid/os/Looper;")
    getThreadId = JavaMethod("()I")
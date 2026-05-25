from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandlerThread"]

class HandlerThread(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/HandlerThread"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    onLooperPrepared = JavaMethod("()V")
    run = JavaMethod("()V")
    getLooper = JavaMethod("()Landroid/os/Looper;")
    quit = JavaMethod("()Z")
    quitSafely = JavaMethod("()Z")
    getThreadId = JavaMethod("()I")
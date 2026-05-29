from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TokenWatcher"]

class TokenWatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/TokenWatcher"
    __javaconstructor__ = [("(Landroid/os/Handler;Ljava/lang/String;)V", False)]
    released = JavaMethod("()V")
    isAcquired = JavaMethod("()Z")
    dump = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/PrintWriter;)V", False, False)])
    cleanup = JavaMethod("(Landroid/os/IBinder;Z)V")
    release = JavaMethod("(Landroid/os/IBinder;)V")
    acquire = JavaMethod("(Landroid/os/IBinder;Ljava/lang/String;)V")
    acquired = JavaMethod("()V")
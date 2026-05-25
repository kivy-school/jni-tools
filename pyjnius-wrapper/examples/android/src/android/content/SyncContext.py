from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncContext"]

class SyncContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncContext"
    onFinished = JavaMethod("(Landroid/content/SyncResult;)V")
    getSyncContextBinder = JavaMethod("()Landroid/os/IBinder;")
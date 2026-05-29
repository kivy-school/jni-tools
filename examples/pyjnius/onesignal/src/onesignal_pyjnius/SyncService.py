from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncService"]

class SyncService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/SyncService"
    __javaconstructor__ = [("()V", False)]
    onStartCommand = JavaMethod("(Landroid/content/Intent;II)I")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
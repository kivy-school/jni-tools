from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceConnection"]

class ServiceConnection(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ServiceConnection"
    onServiceConnected = JavaMethod("(Landroid/content/ComponentName;Landroid/os/IBinder;)V")
    onServiceDisconnected = JavaMethod("(Landroid/content/ComponentName;)V")
    onBindingDied = JavaMethod("(Landroid/content/ComponentName;)V")
    onNullBinding = JavaMethod("(Landroid/content/ComponentName;)V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceConnection"]

class ServiceConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ServiceConnection"
    onNullBinding = JavaMethod("(Landroid/content/ComponentName;)V")
    onBindingDied = JavaMethod("(Landroid/content/ComponentName;)V")
    onServiceConnected = JavaMethod("(Landroid/content/ComponentName;Landroid/os/IBinder;)V")
    onServiceDisconnected = JavaMethod("(Landroid/content/ComponentName;)V")
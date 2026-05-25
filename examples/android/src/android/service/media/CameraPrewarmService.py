from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraPrewarmService"]

class CameraPrewarmService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/media/CameraPrewarmService"
    __javaconstructor__ = [("()V", False)]
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    onPrewarm = JavaMethod("()V")
    onCooldown = JavaMethod("(Z)V")
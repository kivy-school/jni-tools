from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VrListenerService"]

class VrListenerService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/vr/VrListenerService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onCurrentVrActivityChanged = JavaMethod("(Landroid/content/ComponentName;)V")
    isVrModePackageEnabled = JavaStaticMethod("(Landroid/content/Context;Landroid/content/ComponentName;)Z")
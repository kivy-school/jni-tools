from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RestrictionsReceiver"]

class RestrictionsReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/restrictions/RestrictionsReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    onRequestPermission = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/PersistableBundle;)V")
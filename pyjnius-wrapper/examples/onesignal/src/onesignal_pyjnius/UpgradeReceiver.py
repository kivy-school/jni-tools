from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpgradeReceiver"]

class UpgradeReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/UpgradeReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
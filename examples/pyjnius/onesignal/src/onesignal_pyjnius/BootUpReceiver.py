from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BootUpReceiver"]

class BootUpReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/BootUpReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
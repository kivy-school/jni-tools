from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationDismissReceiver"]

class NotificationDismissReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NotificationDismissReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
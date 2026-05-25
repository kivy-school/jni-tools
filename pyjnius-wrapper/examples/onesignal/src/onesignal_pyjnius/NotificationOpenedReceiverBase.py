from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationOpenedReceiverBase"]

class NotificationOpenedReceiverBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NotificationOpenedReceiverBase"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onNewIntent = JavaMethod("(Landroid/content/Intent;)V")
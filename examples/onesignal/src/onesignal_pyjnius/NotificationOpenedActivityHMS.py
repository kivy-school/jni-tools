from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationOpenedActivityHMS"]

class NotificationOpenedActivityHMS(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NotificationOpenedActivityHMS"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onNewIntent = JavaMethod("(Landroid/content/Intent;)V")
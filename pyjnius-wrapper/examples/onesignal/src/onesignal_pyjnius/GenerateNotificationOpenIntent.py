from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenerateNotificationOpenIntent"]

class GenerateNotificationOpenIntent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/GenerateNotificationOpenIntent"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/Intent;Z)V", False)]
    getIntentVisible = JavaMethod("()Landroid/content/Intent;")
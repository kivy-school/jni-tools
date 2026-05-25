from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntentGeneratorForAttachingToNotifications"]

class IntentGeneratorForAttachingToNotifications(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/IntentGeneratorForAttachingToNotifications"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    getContext = JavaMethod("()Landroid/content/Context;")
    getNewBaseIntent = JavaMethod("(I)Landroid/content/Intent;")
    getNewActionPendingIntent = JavaMethod("(ILandroid/content/Intent;)Landroid/app/PendingIntent;")
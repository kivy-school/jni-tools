from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FCMIntentService"]

class FCMIntentService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/FCMIntentService"
    __javaconstructor__ = [("()V", False)]
    onHandleIntent = JavaMethod("(Landroid/content/Intent;)V")
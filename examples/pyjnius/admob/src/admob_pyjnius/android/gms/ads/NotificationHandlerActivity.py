from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationHandlerActivity"]

class NotificationHandlerActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/NotificationHandlerActivity"
    __javaconstructor__ = [("()V", False)]
    CLASS_NAME = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onResume = JavaMethod("()V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FCMIntentJobService"]

class FCMIntentJobService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/FCMIntentJobService"
    __javaconstructor__ = [("()V", False)]
    BUNDLE_EXTRA = JavaStaticField("Ljava/lang/String;")
    onHandleWork = JavaMethod("(Landroid/content/Intent;)V")
    enqueueWork = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
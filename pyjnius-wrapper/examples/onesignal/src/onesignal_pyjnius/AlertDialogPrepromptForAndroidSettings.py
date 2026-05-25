from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlertDialogPrepromptForAndroidSettings"]

class AlertDialogPrepromptForAndroidSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/AlertDialogPrepromptForAndroidSettings"
    INSTANCE = JavaStaticField("Lcom/onesignal/AlertDialogPrepromptForAndroidSettings;")
    show = JavaMethod("(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/AlertDialogPrepromptForAndroidSettings$Callback;)V")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/AlertDialogPrepromptForAndroidSettings/Callback"
        onAccept = JavaMethod("()V")
        onDecline = JavaMethod("()V")
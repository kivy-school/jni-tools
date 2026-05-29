from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationPermissionController"]

class NotificationPermissionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NotificationPermissionController"
    INSTANCE = JavaStaticField("Lcom/onesignal/NotificationPermissionController;")
    prompt = JavaMethod("(ZLcom/onesignal/OneSignal$PromptForPushNotificationPermissionResponseHandler;)V")
    onAccept = JavaMethod("()V")
    onReject = JavaMethod("(Z)V")
    onAppForegrounded = JavaMethod("()V")
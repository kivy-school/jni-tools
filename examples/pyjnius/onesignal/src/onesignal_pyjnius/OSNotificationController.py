from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationController"]

class OSNotificationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationController"
    isNotificationWithinTTL = JavaMethod("()Z")
    getNotificationJob = JavaMethod("()Lcom/onesignal/OSNotificationGenerationJob;")
    getNotificationReceivedEvent = JavaMethod("()Lcom/onesignal/OSNotificationReceivedEvent;")
    isRestoring = JavaMethod("()Z")
    setRestoring = JavaMethod("(Z)V")
    isFromBackgroundLogic = JavaMethod("()Z")
    setFromBackgroundLogic = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")
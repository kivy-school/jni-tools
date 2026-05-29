from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationReceivedEvent"]

class OSNotificationReceivedEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationReceivedEvent"
    complete = JavaMethod("(Lcom/onesignal/OSNotification;)V")
    getNotification = JavaMethod("()Lcom/onesignal/OSNotification;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
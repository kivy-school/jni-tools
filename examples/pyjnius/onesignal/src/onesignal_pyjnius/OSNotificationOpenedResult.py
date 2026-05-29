from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationOpenedResult"]

class OSNotificationOpenedResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationOpenedResult"
    __javaconstructor__ = [("(Lcom/onesignal/OSNotification;Lcom/onesignal/OSNotificationAction;)V", False)]
    onEntryStateChange = JavaMethod("(Lcom/onesignal/OneSignal$AppEntryAction;)V")
    stringify = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getNotification = JavaMethod("()Lcom/onesignal/OSNotification;")
    getAction = JavaMethod("()Lcom/onesignal/OSNotificationAction;")
    toString = JavaMethod("()Ljava/lang/String;")
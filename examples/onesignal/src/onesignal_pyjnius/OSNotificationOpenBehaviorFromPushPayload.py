from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationOpenBehaviorFromPushPayload"]

class OSNotificationOpenBehaviorFromPushPayload(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationOpenBehaviorFromPushPayload"
    __javaconstructor__ = [("(Landroid/content/Context;Lorg/json/JSONObject;)V", False)]
    getShouldOpenApp = JavaMethod("()Z")
    getUri = JavaMethod("()Landroid/net/Uri;")
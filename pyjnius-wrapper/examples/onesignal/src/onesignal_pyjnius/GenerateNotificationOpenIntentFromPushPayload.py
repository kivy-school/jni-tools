from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenerateNotificationOpenIntentFromPushPayload"]

class GenerateNotificationOpenIntentFromPushPayload(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/GenerateNotificationOpenIntentFromPushPayload"
    INSTANCE = JavaStaticField("Lcom/onesignal/GenerateNotificationOpenIntentFromPushPayload;")
    create = JavaMethod("(Landroid/content/Context;Lorg/json/JSONObject;)Lcom/onesignal/GenerateNotificationOpenIntent;")
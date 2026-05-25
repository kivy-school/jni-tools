from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationAction"]

class OSNotificationAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationAction"
    __javaconstructor__ = [("(Lcom/onesignal/OSNotificationAction$ActionType;Ljava/lang/String;)V", False)]
    getType = JavaMethod("()Lcom/onesignal/OSNotificationAction$ActionType;")
    getActionId = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")

    class ActionType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OSNotificationAction/ActionType"
        values = JavaStaticMethod("()[Lcom/onesignal/OSNotificationAction$ActionType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OSNotificationAction$ActionType;")
        Opened = JavaStaticField("Lcom/onesignal/OSNotificationAction/ActionType;")
        ActionTaken = JavaStaticField("Lcom/onesignal/OSNotificationAction/ActionType;")
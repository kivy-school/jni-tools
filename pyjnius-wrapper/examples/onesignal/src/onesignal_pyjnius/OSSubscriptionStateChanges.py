from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSubscriptionStateChanges"]

class OSSubscriptionStateChanges(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSubscriptionStateChanges"
    __javaconstructor__ = [("(Lcom/onesignal/OSSubscriptionState;Lcom/onesignal/OSSubscriptionState;)V", False)]
    getTo = JavaMethod("()Lcom/onesignal/OSSubscriptionState;")
    getFrom = JavaMethod("()Lcom/onesignal/OSSubscriptionState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
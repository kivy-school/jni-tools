from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSEmailSubscriptionStateChanges"]

class OSEmailSubscriptionStateChanges(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSEmailSubscriptionStateChanges"
    __javaconstructor__ = [("(Lcom/onesignal/OSEmailSubscriptionState;Lcom/onesignal/OSEmailSubscriptionState;)V", False)]
    getTo = JavaMethod("()Lcom/onesignal/OSEmailSubscriptionState;")
    getFrom = JavaMethod("()Lcom/onesignal/OSEmailSubscriptionState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSMSSubscriptionStateChanges"]

class OSSMSSubscriptionStateChanges(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSMSSubscriptionStateChanges"
    __javaconstructor__ = [("(Lcom/onesignal/OSSMSSubscriptionState;Lcom/onesignal/OSSMSSubscriptionState;)V", False)]
    getTo = JavaMethod("()Lcom/onesignal/OSSMSSubscriptionState;")
    getFrom = JavaMethod("()Lcom/onesignal/OSSMSSubscriptionState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
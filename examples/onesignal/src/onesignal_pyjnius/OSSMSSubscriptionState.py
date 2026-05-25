from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSMSSubscriptionState"]

class OSSMSSubscriptionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSMSSubscriptionState"
    getSmsUserId = JavaMethod("()Ljava/lang/String;")
    getSMSNumber = JavaMethod("()Ljava/lang/String;")
    isSubscribed = JavaMethod("()Z")
    getObservable = JavaMethod("()Lcom/onesignal/OSObservable;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
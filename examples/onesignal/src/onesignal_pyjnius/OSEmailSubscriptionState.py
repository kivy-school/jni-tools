from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSEmailSubscriptionState"]

class OSEmailSubscriptionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSEmailSubscriptionState"
    getEmailUserId = JavaMethod("()Ljava/lang/String;")
    getEmailAddress = JavaMethod("()Ljava/lang/String;")
    isSubscribed = JavaMethod("()Z")
    getObservable = JavaMethod("()Lcom/onesignal/OSObservable;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
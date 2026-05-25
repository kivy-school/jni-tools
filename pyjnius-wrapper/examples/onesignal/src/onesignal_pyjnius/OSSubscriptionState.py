from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSSubscriptionState"]

class OSSubscriptionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSSubscriptionState"
    getUserId = JavaMethod("()Ljava/lang/String;")
    getPushToken = JavaMethod("()Ljava/lang/String;")
    isPushDisabled = JavaMethod("()Z")
    isSubscribed = JavaMethod("()Z")
    getObservable = JavaMethod("()Lcom/onesignal/OSObservable;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
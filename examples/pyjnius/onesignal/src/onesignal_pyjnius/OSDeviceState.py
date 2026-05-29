from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSDeviceState"]

class OSDeviceState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSDeviceState"
    areNotificationsEnabled = JavaMethod("()Z")
    isPushDisabled = JavaMethod("()Z")
    isSubscribed = JavaMethod("()Z")
    getUserId = JavaMethod("()Ljava/lang/String;")
    getPushToken = JavaMethod("()Ljava/lang/String;")
    isEmailSubscribed = JavaMethod("()Z")
    getEmailUserId = JavaMethod("()Ljava/lang/String;")
    getEmailAddress = JavaMethod("()Ljava/lang/String;")
    isSMSSubscribed = JavaMethod("()Z")
    getSMSUserId = JavaMethod("()Ljava/lang/String;")
    getSMSNumber = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
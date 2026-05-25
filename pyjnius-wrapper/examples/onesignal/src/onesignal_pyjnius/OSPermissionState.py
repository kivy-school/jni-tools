from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSPermissionState"]

class OSPermissionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSPermissionState"
    areNotificationsEnabled = JavaMethod("()Z")
    getObservable = JavaMethod("()Lcom/onesignal/OSObservable;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSPermissionStateChanges"]

class OSPermissionStateChanges(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSPermissionStateChanges"
    __javaconstructor__ = [("(Lcom/onesignal/OSPermissionState;Lcom/onesignal/OSPermissionState;)V", False)]
    getTo = JavaMethod("()Lcom/onesignal/OSPermissionState;")
    getFrom = JavaMethod("()Lcom/onesignal/OSPermissionState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
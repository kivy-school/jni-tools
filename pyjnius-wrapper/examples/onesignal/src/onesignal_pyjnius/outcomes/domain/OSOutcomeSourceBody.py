from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeSourceBody"]

class OSOutcomeSourceBody(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/domain/OSOutcomeSourceBody"
    __javaconstructor__ = [("(Lorg/json/JSONArray;Lorg/json/JSONArray;)V", False), ("(Lorg/json/JSONArray;)V", False), ("()V", False)]
    getNotificationIds = JavaMethod("()Lorg/json/JSONArray;")
    setNotificationIds = JavaMethod("(Lorg/json/JSONArray;)V")
    getInAppMessagesIds = JavaMethod("()Lorg/json/JSONArray;")
    setInAppMessagesIds = JavaMethod("(Lorg/json/JSONArray;)V")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
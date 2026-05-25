from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationIntentExtras"]

class OSNotificationIntentExtras(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationIntentExtras"
    __javaconstructor__ = [("(Lorg/json/JSONArray;Lorg/json/JSONObject;)V", False)]
    getDataArray = JavaMethod("()Lorg/json/JSONArray;")
    setDataArray = JavaMethod("(Lorg/json/JSONArray;)V")
    getJsonData = JavaMethod("()Lorg/json/JSONObject;")
    setJsonData = JavaMethod("(Lorg/json/JSONObject;)V")
    component1 = JavaMethod("()Lorg/json/JSONArray;")
    component2 = JavaMethod("()Lorg/json/JSONObject;")
    copy = JavaMethod("(Lorg/json/JSONArray;Lorg/json/JSONObject;)Lcom/onesignal/OSNotificationIntentExtras;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
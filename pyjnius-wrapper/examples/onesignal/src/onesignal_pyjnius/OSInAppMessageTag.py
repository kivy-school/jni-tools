from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageTag"]

class OSInAppMessageTag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageTag"
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getTagsToAdd = JavaMethod("()Lorg/json/JSONObject;")
    setTagsToAdd = JavaMethod("(Lorg/json/JSONObject;)V")
    getTagsToRemove = JavaMethod("()Lorg/json/JSONArray;")
    setTagsToRemove = JavaMethod("(Lorg/json/JSONArray;)V")
    toString = JavaMethod("()Ljava/lang/String;")
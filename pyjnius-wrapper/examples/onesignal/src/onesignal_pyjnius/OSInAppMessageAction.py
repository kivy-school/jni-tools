from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageAction"]

class OSInAppMessageAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageAction"
    getClickName = JavaMethod("()Ljava/lang/String;")
    getUrlTarget = JavaMethod("()Lcom/onesignal/OSInAppMessageAction$OSInAppMessageActionUrlType;")
    getClickUrl = JavaMethod("()Ljava/lang/String;")
    getOutcomes = JavaMethod("()Ljava/util/List;")
    getPrompts = JavaMethod("()Ljava/util/List;")
    getTags = JavaMethod("()Lcom/onesignal/OSInAppMessageTag;")
    isFirstClick = JavaMethod("()Z")
    doesCloseMessage = JavaMethod("()Z")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")

    class OSInAppMessageActionUrlType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OSInAppMessageAction/OSInAppMessageActionUrlType"
        values = JavaStaticMethod("()[Lcom/onesignal/OSInAppMessageAction$OSInAppMessageActionUrlType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OSInAppMessageAction$OSInAppMessageActionUrlType;")
        toString = JavaMethod("()Ljava/lang/String;")
        fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/OSInAppMessageAction$OSInAppMessageActionUrlType;")
        toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
        IN_APP_WEBVIEW = JavaStaticField("Lcom/onesignal/OSInAppMessageAction/OSInAppMessageActionUrlType;")
        BROWSER = JavaStaticField("Lcom/onesignal/OSInAppMessageAction/OSInAppMessageActionUrlType;")
        REPLACE_CONTENT = JavaStaticField("Lcom/onesignal/OSInAppMessageAction/OSInAppMessageActionUrlType;")
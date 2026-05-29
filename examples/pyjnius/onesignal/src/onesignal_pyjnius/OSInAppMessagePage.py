from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessagePage"]

class OSInAppMessagePage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessagePage"
    __javaconstructor__ = [("(Lorg/json/JSONObject;)V", False)]
    getPageId = JavaMethod("()Ljava/lang/String;")
    setPageId = JavaMethod("(Ljava/lang/String;)V")
    getPageIndex = JavaMethod("()Ljava/lang/String;")
    setPageIndex = JavaMethod("(Ljava/lang/String;)V")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
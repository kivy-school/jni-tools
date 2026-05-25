from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageOutcome"]

class OSInAppMessageOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageOutcome"
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getName = JavaMethod("()Ljava/lang/String;")
    setName = JavaMethod("(Ljava/lang/String;)V")
    getWeight = JavaMethod("()F")
    setWeight = JavaMethod("(F)V")
    isUnique = JavaMethod("()Z")
    setUnique = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")
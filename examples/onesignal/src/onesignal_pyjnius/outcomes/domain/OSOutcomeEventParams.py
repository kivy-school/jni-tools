from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventParams"]

class OSOutcomeEventParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/domain/OSOutcomeEventParams"
    __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/outcomes/domain/OSOutcomeSource;FJ)V", False)]
    getOutcomeId = JavaMethod("()Ljava/lang/String;")
    getOutcomeSource = JavaMethod("()Lcom/onesignal/outcomes/domain/OSOutcomeSource;")
    getWeight = JavaMethod("()F")
    setWeight = JavaMethod("(F)V")
    getTimestamp = JavaMethod("()J")
    setTimestamp = JavaMethod("(J)V")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    isUnattributed = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
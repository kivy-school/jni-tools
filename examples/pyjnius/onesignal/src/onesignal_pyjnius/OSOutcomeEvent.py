from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEvent"]

class OSOutcomeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSOutcomeEvent"
    __javaconstructor__ = [("(Lcom/onesignal/influence/domain/OSInfluenceType;Lorg/json/JSONArray;Ljava/lang/String;JF)V", False)]
    fromOutcomeEventParamsV2toOutcomeEventV1 = JavaStaticMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)Lcom/onesignal/OSOutcomeEvent;")
    getSession = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceType;")
    getNotificationIds = JavaMethod("()Lorg/json/JSONArray;")
    getName = JavaMethod("()Ljava/lang/String;")
    getTimestamp = JavaMethod("()J")
    getWeight = JavaMethod("()F")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toJSONObjectForMeasure = JavaMethod("()Lorg/json/JSONObject;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
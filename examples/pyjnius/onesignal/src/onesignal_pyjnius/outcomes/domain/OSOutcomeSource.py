from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeSource"]

class OSOutcomeSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/domain/OSOutcomeSource"
    __javaconstructor__ = [("(Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;)V", False)]
    getDirectBody = JavaMethod("()Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;")
    setDirectBody = JavaMultipleMethod([("(Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;)V", False, False), ("(Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;)Lcom/onesignal/outcomes/domain/OSOutcomeSource;", False, False)])
    getIndirectBody = JavaMethod("()Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;")
    setIndirectBody = JavaMultipleMethod([("(Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;)V", False, False), ("(Lcom/onesignal/outcomes/domain/OSOutcomeSourceBody;)Lcom/onesignal/outcomes/domain/OSOutcomeSource;", False, False)])
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    toString = JavaMethod("()Ljava/lang/String;")
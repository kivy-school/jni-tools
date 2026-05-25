from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInfluence"]

class OSInfluence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/domain/OSInfluence"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Lcom/onesignal/influence/domain/OSInfluenceChannel;Lcom/onesignal/influence/domain/OSInfluenceType;Lorg/json/JSONArray;)V", False)]
    getInfluenceType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceType;")
    setInfluenceType = JavaMethod("(Lcom/onesignal/influence/domain/OSInfluenceType;)V")
    getInfluenceChannel = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    getIds = JavaMethod("()Lorg/json/JSONArray;")
    setIds = JavaMethod("(Lorg/json/JSONArray;)V")
    getDirectId = JavaMethod("()Ljava/lang/String;")
    copy = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluence;")
    toJSONString = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
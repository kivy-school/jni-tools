from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageTracker"]

class OSInAppMessageTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/data/OSInAppMessageTracker"
    __javaconstructor__ = [("(Lcom/onesignal/influence/data/OSInfluenceDataRepository;Lcom/onesignal/OSLogger;Lcom/onesignal/OSTime;)V", False)]
    getIdTag = JavaMethod("()Ljava/lang/String;")
    getChannelType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    getLastChannelObjectsReceivedByNewId = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONArray;")
    getLastChannelObjects = JavaMethod("()Lorg/json/JSONArray;")
    getChannelLimit = JavaMethod("()I")
    getIndirectAttributionWindow = JavaMethod("()I")
    saveChannelObjects = JavaMethod("(Lorg/json/JSONArray;)V")
    initInfluencedTypeFromCache = JavaMethod("()V")
    addSessionData = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/influence/domain/OSInfluence;)V")
    cacheState = JavaMethod("()V")
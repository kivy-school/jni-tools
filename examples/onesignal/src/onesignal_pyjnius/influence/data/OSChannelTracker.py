from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSChannelTracker"]

class OSChannelTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/data/OSChannelTracker"
    __javaconstructor__ = [("(Lcom/onesignal/influence/data/OSInfluenceDataRepository;Lcom/onesignal/OSLogger;Lcom/onesignal/OSTime;)V", False)]
    getDataRepository = JavaMethod("()Lcom/onesignal/influence/data/OSInfluenceDataRepository;")
    setDataRepository = JavaMethod("(Lcom/onesignal/influence/data/OSInfluenceDataRepository;)V")
    getLogger = JavaMethod("()Lcom/onesignal/OSLogger;")
    setLogger = JavaMethod("(Lcom/onesignal/OSLogger;)V")
    getInfluenceType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceType;")
    setInfluenceType = JavaMethod("(Lcom/onesignal/influence/domain/OSInfluenceType;)V")
    getIndirectIds = JavaMethod("()Lorg/json/JSONArray;")
    setIndirectIds = JavaMethod("(Lorg/json/JSONArray;)V")
    getDirectId = JavaMethod("()Ljava/lang/String;")
    setDirectId = JavaMethod("(Ljava/lang/String;)V")
    getIdTag = JavaMethod("()Ljava/lang/String;")
    getChannelType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    getLastChannelObjects = JavaMethod("()Lorg/json/JSONArray;")
    getChannelLimit = JavaMethod("()I")
    getIndirectAttributionWindow = JavaMethod("()I")
    getLastChannelObjectsReceivedByNewId = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONArray;")
    saveChannelObjects = JavaMethod("(Lorg/json/JSONArray;)V")
    initInfluencedTypeFromCache = JavaMethod("()V")
    cacheState = JavaMethod("()V")
    addSessionData = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/influence/domain/OSInfluence;)V")
    getCurrentSessionInfluence = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluence;")
    getLastReceivedIds = JavaMethod("()Lorg/json/JSONArray;")
    resetAndInitInfluence = JavaMethod("()V")
    saveLastId = JavaMethod("(Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
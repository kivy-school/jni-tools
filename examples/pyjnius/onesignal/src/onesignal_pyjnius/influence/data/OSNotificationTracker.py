from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationTracker"]

class OSNotificationTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/data/OSNotificationTracker"
    __javaconstructor__ = [("(Lcom/onesignal/influence/data/OSInfluenceDataRepository;Lcom/onesignal/OSLogger;Lcom/onesignal/OSTime;)V", False)]
    getLastChannelObjectsReceivedByNewId = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONArray;")
    getLastChannelObjects = JavaMethod("()Lorg/json/JSONArray;")
    getIdTag = JavaMethod("()Ljava/lang/String;")
    getChannelType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    getChannelLimit = JavaMethod("()I")
    getIndirectAttributionWindow = JavaMethod("()I")
    saveChannelObjects = JavaMethod("(Lorg/json/JSONArray;)V")
    initInfluencedTypeFromCache = JavaMethod("()V")
    addSessionData = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/influence/domain/OSInfluence;)V")
    cacheState = JavaMethod("()V")
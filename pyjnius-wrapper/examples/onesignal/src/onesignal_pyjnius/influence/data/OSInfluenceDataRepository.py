from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInfluenceDataRepository"]

class OSInfluenceDataRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/data/OSInfluenceDataRepository"
    __javaconstructor__ = [("(Lcom/onesignal/OSSharedPreferences;)V", False)]
    cacheNotificationInfluenceType = JavaMethod("(Lcom/onesignal/influence/domain/OSInfluenceType;)V")
    getNotificationCachedInfluenceType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceType;")
    cacheIAMInfluenceType = JavaMethod("(Lcom/onesignal/influence/domain/OSInfluenceType;)V")
    getIamCachedInfluenceType = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceType;")
    cacheNotificationOpenId = JavaMethod("(Ljava/lang/String;)V")
    getCachedNotificationOpenId = JavaMethod("()Ljava/lang/String;")
    saveNotifications = JavaMethod("(Lorg/json/JSONArray;)V")
    saveIAMs = JavaMethod("(Lorg/json/JSONArray;)V")
    getLastNotificationsReceivedData = JavaMethod("()Lorg/json/JSONArray;")
    getLastIAMsReceivedData = JavaMethod("()Lorg/json/JSONArray;")
    getNotificationLimit = JavaMethod("()I")
    getIamLimit = JavaMethod("()I")
    getNotificationIndirectAttributionWindow = JavaMethod("()I")
    getIamIndirectAttributionWindow = JavaMethod("()I")
    isDirectInfluenceEnabled = JavaMethod("()Z")
    isIndirectInfluenceEnabled = JavaMethod("()Z")
    isUnattributedInfluenceEnabled = JavaMethod("()Z")
    saveInfluenceParams = JavaMethod("(Lcom/onesignal/OneSignalRemoteParams$InfluenceParams;)V")
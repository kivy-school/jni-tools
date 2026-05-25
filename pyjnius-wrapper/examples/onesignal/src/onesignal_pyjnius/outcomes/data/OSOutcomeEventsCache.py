from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsCache"]

class OSOutcomeEventsCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsCache"
    __javaconstructor__ = [("(Lcom/onesignal/OSLogger;Lcom/onesignal/OneSignalDb;Lcom/onesignal/OSSharedPreferences;)V", False)]
    isOutcomesV2ServiceEnabled = JavaMethod("()Z")
    getUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("()Ljava/util/Set;")
    saveUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("(Ljava/util/Set;)V")
    deleteOldOutcomeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    saveOutcomeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    getAllEventsToSend = JavaMethod("()Ljava/util/List;")
    saveUniqueOutcomeEventParams = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    getNotCachedUniqueInfluencesForOutcome = JavaMethod("(Ljava/lang/String;Ljava/util/List;)Ljava/util/List;")
    cleanCachedUniqueOutcomeEventNotifications = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsCache/WhenMappings"
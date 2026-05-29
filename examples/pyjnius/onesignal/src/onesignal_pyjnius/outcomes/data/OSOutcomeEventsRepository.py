from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsRepository"]

class OSOutcomeEventsRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsRepository"
    __javaconstructor__ = [("(Lcom/onesignal/OSLogger;Lcom/onesignal/outcomes/data/OSOutcomeEventsCache;Lcom/onesignal/outcomes/data/OutcomeEventsService;)V", False)]
    getLogger = JavaMethod("()Lcom/onesignal/OSLogger;")
    getOutcomeEventsService = JavaMethod("()Lcom/onesignal/outcomes/data/OutcomeEventsService;")
    requestMeasureOutcomeEvent = JavaMethod("(Ljava/lang/String;ILcom/onesignal/outcomes/domain/OSOutcomeEventParams;Lcom/onesignal/OneSignalApiResponseHandler;)V")
    getSavedOutcomeEvents = JavaMethod("()Ljava/util/List;")
    saveOutcomeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    removeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    saveUniqueOutcomeNotifications = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    getNotCachedUniqueOutcome = JavaMethod("(Ljava/lang/String;Ljava/util/List;)Ljava/util/List;")
    getUnattributedUniqueOutcomeEventsSent = JavaMethod("()Ljava/util/Set;")
    saveUnattributedUniqueOutcomeEventsSent = JavaMethod("(Ljava/util/Set;)V")
    cleanCachedUniqueOutcomeEventNotifications = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
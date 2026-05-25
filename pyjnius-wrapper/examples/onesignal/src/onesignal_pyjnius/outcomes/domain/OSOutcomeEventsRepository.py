from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsRepository"]

class OSOutcomeEventsRepository(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/domain/OSOutcomeEventsRepository"
    getSavedOutcomeEvents = JavaMethod("()Ljava/util/List;")
    saveOutcomeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    removeEvent = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    requestMeasureOutcomeEvent = JavaMethod("(Ljava/lang/String;ILcom/onesignal/outcomes/domain/OSOutcomeEventParams;Lcom/onesignal/OneSignalApiResponseHandler;)V")
    saveUniqueOutcomeNotifications = JavaMethod("(Lcom/onesignal/outcomes/domain/OSOutcomeEventParams;)V")
    getNotCachedUniqueOutcome = JavaMethod("(Ljava/lang/String;Ljava/util/List;)Ljava/util/List;")
    getUnattributedUniqueOutcomeEventsSent = JavaMethod("()Ljava/util/Set;")
    saveUnattributedUniqueOutcomeEventsSent = JavaMethod("(Ljava/util/Set;)V")
    cleanCachedUniqueOutcomeEventNotifications = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
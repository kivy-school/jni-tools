from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsV2Repository"]

class OSOutcomeEventsV2Repository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsV2Repository"
    __javaconstructor__ = [("(Lcom/onesignal/OSLogger;Lcom/onesignal/outcomes/data/OSOutcomeEventsCache;Lcom/onesignal/outcomes/data/OutcomeEventsService;)V", False)]
    requestMeasureOutcomeEvent = JavaMethod("(Ljava/lang/String;ILcom/onesignal/outcomes/domain/OSOutcomeEventParams;Lcom/onesignal/OneSignalApiResponseHandler;)V")
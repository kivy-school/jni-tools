from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutcomeEventsService"]

class OutcomeEventsService(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OutcomeEventsService"
    sendOutcomeEvent = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
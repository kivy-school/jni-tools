from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsV1Service"]

class OSOutcomeEventsV1Service(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsV1Service"
    __javaconstructor__ = [("(Lcom/onesignal/OneSignalAPIClient;)V", False)]
    sendOutcomeEvent = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
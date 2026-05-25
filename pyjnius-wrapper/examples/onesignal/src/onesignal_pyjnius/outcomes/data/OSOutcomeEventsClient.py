from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeEventsClient"]

class OSOutcomeEventsClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OSOutcomeEventsClient"
    __javaconstructor__ = [("(Lcom/onesignal/OneSignalAPIClient;)V", False)]
    getClient = JavaMethod("()Lcom/onesignal/OneSignalAPIClient;")
    sendOutcomeEvent = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
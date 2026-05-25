from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalAPIClient"]

class OneSignalAPIClient(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalAPIClient"
    put = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
    post = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
    get = JavaMethod("(Ljava/lang/String;Lcom/onesignal/OneSignalApiResponseHandler;Ljava/lang/String;)V")
    getSync = JavaMethod("(Ljava/lang/String;Lcom/onesignal/OneSignalApiResponseHandler;Ljava/lang/String;)V")
    putSync = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
    postSync = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/OneSignalApiResponseHandler;)V")
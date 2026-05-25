from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalApiResponseHandler"]

class OneSignalApiResponseHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalApiResponseHandler"
    onSuccess = JavaMethod("(Ljava/lang/String;)V")
    onFailure = JavaMethod("(ILjava/lang/String;Ljava/lang/Throwable;)V")
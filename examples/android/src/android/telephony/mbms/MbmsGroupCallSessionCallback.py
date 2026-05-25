from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsGroupCallSessionCallback"]

class MbmsGroupCallSessionCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsGroupCallSessionCallback"
    onError = JavaMethod("(ILjava/lang/String;)V")
    onAvailableSaisUpdated = JavaMethod("(Ljava/util/List;Ljava/util/List;)V")
    onServiceInterfaceAvailable = JavaMethod("(Ljava/lang/String;I)V")
    onMiddlewareReady = JavaMethod("()V")
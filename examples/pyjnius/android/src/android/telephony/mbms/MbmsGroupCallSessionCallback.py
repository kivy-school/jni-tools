from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsGroupCallSessionCallback"]

class MbmsGroupCallSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsGroupCallSessionCallback"
    onAvailableSaisUpdated = JavaMethod("(Ljava/util/List;Ljava/util/List;)V")
    onMiddlewareReady = JavaMethod("()V")
    onServiceInterfaceAvailable = JavaMethod("(Ljava/lang/String;I)V")
    onError = JavaMethod("(ILjava/lang/String;)V")
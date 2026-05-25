from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsStreamingSessionCallback"]

class MbmsStreamingSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsStreamingSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onError = JavaMethod("(ILjava/lang/String;)V")
    onStreamingServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onMiddlewareReady = JavaMethod("()V")
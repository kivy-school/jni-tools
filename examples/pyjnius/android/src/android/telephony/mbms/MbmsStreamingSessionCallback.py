from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsStreamingSessionCallback"]

class MbmsStreamingSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsStreamingSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onMiddlewareReady = JavaMethod("()V")
    onStreamingServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onError = JavaMethod("(ILjava/lang/String;)V")
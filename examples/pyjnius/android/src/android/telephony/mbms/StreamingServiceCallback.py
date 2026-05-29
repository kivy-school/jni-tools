from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamingServiceCallback"]

class StreamingServiceCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingServiceCallback"
    __javaconstructor__ = [("()V", False)]
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onMediaDescriptionUpdated = JavaMethod("()V")
    onStreamMethodUpdated = JavaMethod("(I)V")
    onStreamStateUpdated = JavaMethod("(II)V")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")
    onError = JavaMethod("(ILjava/lang/String;)V")
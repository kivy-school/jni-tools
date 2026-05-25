from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamingServiceCallback"]

class StreamingServiceCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingServiceCallback"
    __javaconstructor__ = [("()V", False)]
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onError = JavaMethod("(ILjava/lang/String;)V")
    onStreamStateUpdated = JavaMethod("(II)V")
    onMediaDescriptionUpdated = JavaMethod("()V")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")
    onStreamMethodUpdated = JavaMethod("(I)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallEventCallback"]

class CallEventCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallEventCallback"
    onCallEndpointChanged = JavaMethod("(Landroid/telecom/CallEndpoint;)V")
    onAvailableCallEndpointsChanged = JavaMethod("(Ljava/util/List;)V")
    onMuteStateChanged = JavaMethod("(Z)V")
    onVideoStateChanged = JavaMethod("(I)V")
    onCallStreamingFailed = JavaMethod("(I)V")
    onEvent = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
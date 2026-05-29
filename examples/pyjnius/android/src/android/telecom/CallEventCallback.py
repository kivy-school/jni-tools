from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallEventCallback"]

class CallEventCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallEventCallback"
    onVideoStateChanged = JavaMethod("(I)V")
    onCallStreamingFailed = JavaMethod("(I)V")
    onAvailableCallEndpointsChanged = JavaMethod("(Ljava/util/List;)V")
    onCallEndpointChanged = JavaMethod("(Landroid/telecom/CallEndpoint;)V")
    onMuteStateChanged = JavaMethod("(Z)V")
    onEvent = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
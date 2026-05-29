from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallControl"]

class CallControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallControl"
    getCallId = JavaMethod("()Landroid/os/ParcelUuid;")
    disconnect = JavaMethod("(Landroid/telecom/DisconnectCause;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    setActive = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestCallEndpointChange = JavaMethod("(Landroid/telecom/CallEndpoint;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    answer = JavaMethod("(ILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    setInactive = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestMuteState = JavaMethod("(ZLjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestVideoState = JavaMethod("(ILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    sendEvent = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
    startCallStreaming = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteConference"]

class RemoteConference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/RemoteConference"
    getConnections = JavaMethod("()Ljava/util/List;")
    getState = JavaMethod("()I")
    getConnectionCapabilities = JavaMethod("()I")
    getConnectionProperties = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    disconnect = JavaMethod("()V")
    separate = JavaMethod("(Landroid/telecom/RemoteConnection;)V")
    merge = JavaMethod("()V")
    swap = JavaMethod("()V")
    hold = JavaMethod("()V")
    unhold = JavaMethod("()V")
    getDisconnectCause = JavaMethod("()Landroid/telecom/DisconnectCause;")
    playDtmfTone = JavaMethod("(C)V")
    stopDtmfTone = JavaMethod("()V")
    setCallAudioState = JavaMethod("(Landroid/telecom/CallAudioState;)V")
    getConferenceableConnections = JavaMethod("()Ljava/util/List;")
    registerCallback = JavaMultipleMethod([("(Landroid/telecom/RemoteConference$Callback;)V", False, False), ("(Landroid/telecom/RemoteConference$Callback;Landroid/os/Handler;)V", False, False)])
    unregisterCallback = JavaMethod("(Landroid/telecom/RemoteConference$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/RemoteConference/Callback"
        __javaconstructor__ = [("()V", False)]
        onStateChanged = JavaMethod("(Landroid/telecom/RemoteConference;II)V")
        onDisconnected = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/DisconnectCause;)V")
        onConnectionAdded = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/RemoteConnection;)V")
        onConnectionRemoved = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/RemoteConnection;)V")
        onConnectionCapabilitiesChanged = JavaMethod("(Landroid/telecom/RemoteConference;I)V")
        onConnectionPropertiesChanged = JavaMethod("(Landroid/telecom/RemoteConference;I)V")
        onConferenceableConnectionsChanged = JavaMethod("(Landroid/telecom/RemoteConference;Ljava/util/List;)V")
        onDestroyed = JavaMethod("(Landroid/telecom/RemoteConference;)V")
        onExtrasChanged = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/os/Bundle;)V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteConference"]

class RemoteConference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/RemoteConference"
    separate = JavaMethod("(Landroid/telecom/RemoteConnection;)V")
    setCallAudioState = JavaMethod("(Landroid/telecom/CallAudioState;)V")
    disconnect = JavaMethod("()V")
    merge = JavaMethod("()V")
    getState = JavaMethod("()I")
    getDisconnectCause = JavaMethod("()Landroid/telecom/DisconnectCause;")
    getConnections = JavaMethod("()Ljava/util/List;")
    getConferenceableConnections = JavaMethod("()Ljava/util/List;")
    getConnectionCapabilities = JavaMethod("()I")
    getConnectionProperties = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    swap = JavaMethod("()V")
    registerCallback = JavaMultipleMethod([("(Landroid/telecom/RemoteConference$Callback;Landroid/os/Handler;)V", False, False), ("(Landroid/telecom/RemoteConference$Callback;)V", False, False)])
    unregisterCallback = JavaMethod("(Landroid/telecom/RemoteConference$Callback;)V")
    hold = JavaMethod("()V")
    playDtmfTone = JavaMethod("(C)V")
    stopDtmfTone = JavaMethod("()V")
    unhold = JavaMethod("()V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/RemoteConference$Callback"
        __javaconstructor__ = [("()V", False)]
        onDisconnected = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/DisconnectCause;)V")
        onConferenceableConnectionsChanged = JavaMethod("(Landroid/telecom/RemoteConference;Ljava/util/List;)V")
        onConnectionCapabilitiesChanged = JavaMethod("(Landroid/telecom/RemoteConference;I)V")
        onConnectionPropertiesChanged = JavaMethod("(Landroid/telecom/RemoteConference;I)V")
        onConnectionRemoved = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/RemoteConnection;)V")
        onConnectionAdded = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/telecom/RemoteConnection;)V")
        onExtrasChanged = JavaMethod("(Landroid/telecom/RemoteConference;Landroid/os/Bundle;)V")
        onStateChanged = JavaMethod("(Landroid/telecom/RemoteConference;II)V")
        onDestroyed = JavaMethod("(Landroid/telecom/RemoteConference;)V")
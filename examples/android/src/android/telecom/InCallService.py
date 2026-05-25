from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InCallService"]

class InCallService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/InCallService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    getCalls = JavaMethod("()Ljava/util/List;")
    canAddCall = JavaMethod("()Z")
    getCallAudioState = JavaMethod("()Landroid/telecom/CallAudioState;")
    setMuted = JavaMethod("(Z)V")
    setAudioRoute = JavaMethod("(I)V")
    requestBluetoothAudio = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)V")
    requestCallEndpointChange = JavaMethod("(Landroid/telecom/CallEndpoint;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getCurrentCallEndpoint = JavaMethod("()Landroid/telecom/CallEndpoint;")
    onCallAudioStateChanged = JavaMethod("(Landroid/telecom/CallAudioState;)V")
    onCallEndpointChanged = JavaMethod("(Landroid/telecom/CallEndpoint;)V")
    onAvailableCallEndpointsChanged = JavaMethod("(Ljava/util/List;)V")
    onMuteStateChanged = JavaMethod("(Z)V")
    onBringToForeground = JavaMethod("(Z)V")
    onCallAdded = JavaMethod("(Landroid/telecom/Call;)V")
    onCallRemoved = JavaMethod("(Landroid/telecom/Call;)V")
    onCanAddCallChanged = JavaMethod("(Z)V")
    onSilenceRinger = JavaMethod("()V")
    onConnectionEvent = JavaMethod("(Landroid/telecom/Call;Ljava/lang/String;Landroid/os/Bundle;)V")

    class VideoCall(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/InCallService/VideoCall"
        __javaconstructor__ = [("()V", False)]
        registerCallback = JavaMultipleMethod([("(Landroid/telecom/InCallService$VideoCall$Callback;)V", False, False), ("(Landroid/telecom/InCallService$VideoCall$Callback;Landroid/os/Handler;)V", False, False)])
        unregisterCallback = JavaMethod("(Landroid/telecom/InCallService$VideoCall$Callback;)V")
        setCamera = JavaMethod("(Ljava/lang/String;)V")
        setPreviewSurface = JavaMethod("(Landroid/view/Surface;)V")
        setDisplaySurface = JavaMethod("(Landroid/view/Surface;)V")
        setDeviceOrientation = JavaMethod("(I)V")
        setZoom = JavaMethod("(F)V")
        sendSessionModifyRequest = JavaMethod("(Landroid/telecom/VideoProfile;)V")
        sendSessionModifyResponse = JavaMethod("(Landroid/telecom/VideoProfile;)V")
        requestCameraCapabilities = JavaMethod("()V")
        requestCallDataUsage = JavaMethod("()V")
        setPauseImage = JavaMethod("(Landroid/net/Uri;)V")

        class Callback(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/telecom/InCallService/VideoCall/Callback"
            __javaconstructor__ = [("()V", False)]
            onSessionModifyRequestReceived = JavaMethod("(Landroid/telecom/VideoProfile;)V")
            onSessionModifyResponseReceived = JavaMethod("(ILandroid/telecom/VideoProfile;Landroid/telecom/VideoProfile;)V")
            onCallSessionEvent = JavaMethod("(I)V")
            onPeerDimensionsChanged = JavaMethod("(II)V")
            onVideoQualityChanged = JavaMethod("(I)V")
            onCallDataUsageChanged = JavaMethod("(J)V")
            onCameraCapabilitiesChanged = JavaMethod("(Landroid/telecom/VideoProfile$CameraCapabilities;)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipAudioCall"]

class SipAudioCall(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipAudioCall"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/net/sip/SipProfile;)V", False)]
    setListener = JavaMultipleMethod([("(Landroid/net/sip/SipAudioCall$Listener;)V", False, False), ("(Landroid/net/sip/SipAudioCall$Listener;Z)V", False, False)])
    isInCall = JavaMethod("()Z")
    isOnHold = JavaMethod("()Z")
    close = JavaMethod("()V")
    getLocalProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    getPeerProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    getState = JavaMethod("()I")
    attachCall = JavaMethod("(Landroid/net/sip/SipSession;Ljava/lang/String;)V")
    makeCall = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipSession;I)V")
    endCall = JavaMethod("()V")
    holdCall = JavaMethod("(I)V")
    answerCall = JavaMethod("(I)V")
    continueCall = JavaMethod("(I)V")
    toggleMute = JavaMethod("()V")
    isMuted = JavaMethod("()Z")
    setSpeakerMode = JavaMethod("(Z)V")
    sendDtmf = JavaMultipleMethod([("(I)V", False, False), ("(ILandroid/os/Message;)V", False, False)])
    startAudio = JavaMethod("()V")

    class Listener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipAudioCall/Listener"
        __javaconstructor__ = [("()V", False)]
        onReadyToCall = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCalling = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onRinging = JavaMethod("(Landroid/net/sip/SipAudioCall;Landroid/net/sip/SipProfile;)V")
        onRingingBack = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallEstablished = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallEnded = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallBusy = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallHeld = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onError = JavaMethod("(Landroid/net/sip/SipAudioCall;ILjava/lang/String;)V")
        onChanged = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
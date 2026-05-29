from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipAudioCall"]

class SipAudioCall(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipAudioCall"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/net/sip/SipProfile;)V", False)]
    setListener = JavaMultipleMethod([("(Landroid/net/sip/SipAudioCall$Listener;Z)V", False, False), ("(Landroid/net/sip/SipAudioCall$Listener;)V", False, False)])
    getPeerProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    getLocalProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    answerCall = JavaMethod("(I)V")
    makeCall = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipSession;I)V")
    attachCall = JavaMethod("(Landroid/net/sip/SipSession;Ljava/lang/String;)V")
    continueCall = JavaMethod("(I)V")
    holdCall = JavaMethod("(I)V")
    isOnHold = JavaMethod("()Z")
    setSpeakerMode = JavaMethod("(Z)V")
    startAudio = JavaMethod("()V")
    toggleMute = JavaMethod("()V")
    endCall = JavaMethod("()V")
    isInCall = JavaMethod("()Z")
    sendDtmf = JavaMultipleMethod([("(I)V", False, False), ("(ILandroid/os/Message;)V", False, False)])
    close = JavaMethod("()V")
    getState = JavaMethod("()I")
    isMuted = JavaMethod("()Z")

    class Listener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipAudioCall$Listener"
        __javaconstructor__ = [("()V", False)]
        onCallHeld = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onReadyToCall = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallBusy = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallEnded = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCallEstablished = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onCalling = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onRinging = JavaMethod("(Landroid/net/sip/SipAudioCall;Landroid/net/sip/SipProfile;)V")
        onRingingBack = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
        onError = JavaMethod("(Landroid/net/sip/SipAudioCall;ILjava/lang/String;)V")
        onChanged = JavaMethod("(Landroid/net/sip/SipAudioCall;)V")
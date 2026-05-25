from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipSession"]

class SipSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipSession"
    getLocalIp = JavaMethod("()Ljava/lang/String;")
    getLocalProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    getPeerProfile = JavaMethod("()Landroid/net/sip/SipProfile;")
    getState = JavaMethod("()I")
    isInCall = JavaMethod("()Z")
    getCallId = JavaMethod("()Ljava/lang/String;")
    setListener = JavaMethod("(Landroid/net/sip/SipSession$Listener;)V")
    register = JavaMethod("(I)V")
    unregister = JavaMethod("()V")
    makeCall = JavaMethod("(Landroid/net/sip/SipProfile;Ljava/lang/String;I)V")
    answerCall = JavaMethod("(Ljava/lang/String;I)V")
    endCall = JavaMethod("()V")
    changeCall = JavaMethod("(Ljava/lang/String;I)V")

    class Listener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipSession/Listener"
        __javaconstructor__ = [("()V", False)]
        onCalling = JavaMethod("(Landroid/net/sip/SipSession;)V")
        onRinging = JavaMethod("(Landroid/net/sip/SipSession;Landroid/net/sip/SipProfile;Ljava/lang/String;)V")
        onRingingBack = JavaMethod("(Landroid/net/sip/SipSession;)V")
        onCallEstablished = JavaMethod("(Landroid/net/sip/SipSession;Ljava/lang/String;)V")
        onCallEnded = JavaMethod("(Landroid/net/sip/SipSession;)V")
        onCallBusy = JavaMethod("(Landroid/net/sip/SipSession;)V")
        onError = JavaMethod("(Landroid/net/sip/SipSession;ILjava/lang/String;)V")
        onCallChangeFailed = JavaMethod("(Landroid/net/sip/SipSession;ILjava/lang/String;)V")
        onRegistering = JavaMethod("(Landroid/net/sip/SipSession;)V")
        onRegistrationDone = JavaMethod("(Landroid/net/sip/SipSession;I)V")
        onRegistrationFailed = JavaMethod("(Landroid/net/sip/SipSession;ILjava/lang/String;)V")
        onRegistrationTimeout = JavaMethod("(Landroid/net/sip/SipSession;)V")

    class State(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipSession/State"
        DEREGISTERING = JavaStaticField("I")
        INCOMING_CALL = JavaStaticField("I")
        INCOMING_CALL_ANSWERING = JavaStaticField("I")
        IN_CALL = JavaStaticField("I")
        NOT_DEFINED = JavaStaticField("I")
        OUTGOING_CALL = JavaStaticField("I")
        OUTGOING_CALL_CANCELING = JavaStaticField("I")
        OUTGOING_CALL_RING_BACK = JavaStaticField("I")
        PINGING = JavaStaticField("I")
        READY_TO_CALL = JavaStaticField("I")
        REGISTERING = JavaStaticField("I")
        toString = JavaStaticMethod("(I)Ljava/lang/String;")
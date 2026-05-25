from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipManager"]

class SipManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipManager"
    EXTRA_CALL_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_OFFER_SD = JavaStaticField("Ljava/lang/String;")
    INCOMING_CALL_RESULT_CODE = JavaStaticField("I")
    newInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/net/sip/SipManager;")
    isApiSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    isVoipSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    isSipWifiOnly = JavaStaticMethod("(Landroid/content/Context;)Z")
    open = JavaMultipleMethod([("(Landroid/net/sip/SipProfile;)V", False, False), ("(Landroid/net/sip/SipProfile;Landroid/app/PendingIntent;Landroid/net/sip/SipRegistrationListener;)V", False, False)])
    setRegistrationListener = JavaMethod("(Ljava/lang/String;Landroid/net/sip/SipRegistrationListener;)V")
    close = JavaMethod("(Ljava/lang/String;)V")
    isOpened = JavaMethod("(Ljava/lang/String;)Z")
    isRegistered = JavaMethod("(Ljava/lang/String;)Z")
    makeAudioCall = JavaMultipleMethod([("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipProfile;Landroid/net/sip/SipAudioCall$Listener;I)Landroid/net/sip/SipAudioCall;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/net/sip/SipAudioCall$Listener;I)Landroid/net/sip/SipAudioCall;", False, False)])
    takeAudioCall = JavaMethod("(Landroid/content/Intent;Landroid/net/sip/SipAudioCall$Listener;)Landroid/net/sip/SipAudioCall;")
    isIncomingCallIntent = JavaStaticMethod("(Landroid/content/Intent;)Z")
    getCallId = JavaStaticMethod("(Landroid/content/Intent;)Ljava/lang/String;")
    getOfferSessionDescription = JavaStaticMethod("(Landroid/content/Intent;)Ljava/lang/String;")
    register = JavaMethod("(Landroid/net/sip/SipProfile;ILandroid/net/sip/SipRegistrationListener;)V")
    unregister = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipRegistrationListener;)V")
    getSessionFor = JavaMethod("(Landroid/content/Intent;)Landroid/net/sip/SipSession;")
    createSipSession = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipSession$Listener;)Landroid/net/sip/SipSession;")
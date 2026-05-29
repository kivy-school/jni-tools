from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipManager"]

class SipManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipManager"
    EXTRA_CALL_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_OFFER_SD = JavaStaticField("Ljava/lang/String;")
    INCOMING_CALL_RESULT_CODE = JavaStaticField("I")
    getCallId = JavaStaticMethod("(Landroid/content/Intent;)Ljava/lang/String;")
    createSipSession = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipSession$Listener;)Landroid/net/sip/SipSession;")
    getOfferSessionDescription = JavaStaticMethod("(Landroid/content/Intent;)Ljava/lang/String;")
    getSessionFor = JavaMethod("(Landroid/content/Intent;)Landroid/net/sip/SipSession;")
    isApiSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    isIncomingCallIntent = JavaStaticMethod("(Landroid/content/Intent;)Z")
    isSipWifiOnly = JavaStaticMethod("(Landroid/content/Context;)Z")
    isVoipSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    makeAudioCall = JavaMultipleMethod([("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipProfile;Landroid/net/sip/SipAudioCall$Listener;I)Landroid/net/sip/SipAudioCall;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/net/sip/SipAudioCall$Listener;I)Landroid/net/sip/SipAudioCall;", False, False)])
    setRegistrationListener = JavaMethod("(Ljava/lang/String;Landroid/net/sip/SipRegistrationListener;)V")
    takeAudioCall = JavaMethod("(Landroid/content/Intent;Landroid/net/sip/SipAudioCall$Listener;)Landroid/net/sip/SipAudioCall;")
    newInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/net/sip/SipManager;")
    isRegistered = JavaMethod("(Ljava/lang/String;)Z")
    close = JavaMethod("(Ljava/lang/String;)V")
    register = JavaMethod("(Landroid/net/sip/SipProfile;ILandroid/net/sip/SipRegistrationListener;)V")
    open = JavaMultipleMethod([("(Landroid/net/sip/SipProfile;)V", False, False), ("(Landroid/net/sip/SipProfile;Landroid/app/PendingIntent;Landroid/net/sip/SipRegistrationListener;)V", False, False)])
    isOpened = JavaMethod("(Ljava/lang/String;)Z")
    unregister = JavaMethod("(Landroid/net/sip/SipProfile;Landroid/net/sip/SipRegistrationListener;)V")
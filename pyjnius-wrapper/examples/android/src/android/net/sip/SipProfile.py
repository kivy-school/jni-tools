from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipProfile"]

class SipProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipProfile"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getUriString = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    getUserName = JavaMethod("()Ljava/lang/String;")
    getAuthUserName = JavaMethod("()Ljava/lang/String;")
    getPassword = JavaMethod("()Ljava/lang/String;")
    getSipDomain = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getProxyAddress = JavaMethod("()Ljava/lang/String;")
    getProfileName = JavaMethod("()Ljava/lang/String;")
    getSendKeepAlive = JavaMethod("()Z")
    getAutoRegistration = JavaMethod("()Z")
    setCallingUid = JavaMethod("(I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipProfile/Builder"
        __javaconstructor__ = [("(Landroid/net/sip/SipProfile;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setAuthUserName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setProfileName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setPassword = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setPort = JavaMethod("(I)Landroid/net/sip/SipProfile$Builder;")
        setProtocol = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setOutboundProxy = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setSendKeepAlive = JavaMethod("(Z)Landroid/net/sip/SipProfile$Builder;")
        setAutoRegistration = JavaMethod("(Z)Landroid/net/sip/SipProfile$Builder;")
        build = JavaMethod("()Landroid/net/sip/SipProfile;")
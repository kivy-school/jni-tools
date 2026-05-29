from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipProfile"]

class SipProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipProfile"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPassword = JavaMethod("()Ljava/lang/String;")
    getProxyAddress = JavaMethod("()Ljava/lang/String;")
    getSipDomain = JavaMethod("()Ljava/lang/String;")
    getSendKeepAlive = JavaMethod("()Z")
    getAuthUserName = JavaMethod("()Ljava/lang/String;")
    getProfileName = JavaMethod("()Ljava/lang/String;")
    getAutoRegistration = JavaMethod("()Z")
    getUriString = JavaMethod("()Ljava/lang/String;")
    getUserName = JavaMethod("()Ljava/lang/String;")
    setCallingUid = JavaMethod("(I)V")
    getPort = JavaMethod("()I")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/sip/SipProfile$Builder"
        __javaconstructor__ = [("(Landroid/net/sip/SipProfile;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setPort = JavaMethod("(I)Landroid/net/sip/SipProfile$Builder;")
        setProtocol = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setSendKeepAlive = JavaMethod("(Z)Landroid/net/sip/SipProfile$Builder;")
        setAuthUserName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setAutoRegistration = JavaMethod("(Z)Landroid/net/sip/SipProfile$Builder;")
        setOutboundProxy = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setProfileName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setPassword = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/String;)Landroid/net/sip/SipProfile$Builder;")
        build = JavaMethod("()Landroid/net/sip/SipProfile;")
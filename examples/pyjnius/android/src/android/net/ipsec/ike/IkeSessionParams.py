from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionParams"]

class IkeSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionParams"
    IKE_DPD_DELAY_SEC_DISABLED = JavaStaticField("I")
    IKE_OPTION_ACCEPT_ANY_REMOTE_ID = JavaStaticField("I")
    IKE_OPTION_EAP_ONLY_AUTH = JavaStaticField("I")
    IKE_OPTION_FORCE_PORT_4500 = JavaStaticField("I")
    IKE_OPTION_INITIAL_CONTACT = JavaStaticField("I")
    IKE_OPTION_MOBIKE = JavaStaticField("I")
    getNetwork = JavaMethod("()Landroid/net/Network;")
    getHardLifetimeSeconds = JavaMethod("()I")
    getSoftLifetimeSeconds = JavaMethod("()I")
    getDpdDelaySeconds = JavaMethod("()I")
    getIkeOptions = JavaMethod("()Ljava/util/Set;")
    getIkeSaProposals = JavaMethod("()Ljava/util/List;")
    getLocalAuthConfig = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams$IkeAuthConfig;")
    getLocalIdentification = JavaMethod("()Landroid/net/ipsec/ike/IkeIdentification;")
    getNattKeepAliveDelaySeconds = JavaMethod("()I")
    getRemoteAuthConfig = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams$IkeAuthConfig;")
    getRemoteIdentification = JavaMethod("()Landroid/net/ipsec/ike/IkeIdentification;")
    getRetransmissionTimeoutsMillis = JavaMethod("()[I")
    getServerHostname = JavaMethod("()Ljava/lang/String;")
    hasIkeOption = JavaMethod("(I)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class IkeAuthPskConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$IkeAuthPskConfig"
        getPsk = JavaMethod("()[B")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class IkeAuthEapConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$IkeAuthEapConfig"
        getEapConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class IkeAuthDigitalSignRemoteConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$IkeAuthDigitalSignRemoteConfig"
        getRemoteCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class IkeAuthDigitalSignLocalConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$IkeAuthDigitalSignLocalConfig"
        getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
        getClientEndCertificate = JavaMethod("()Ljava/security/cert/X509Certificate;")
        getIntermediateCertificates = JavaMethod("()Ljava/util/List;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class IkeAuthConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$IkeAuthConfig"
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionParams$Builder"
        __javaconstructor__ = [("(Landroid/net/ipsec/ike/IkeSessionParams;)V", False), ("()V", False)]
        setAuthDigitalSignature = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;", False, False), ("(Ljava/security/cert/X509Certificate;Ljava/security/cert/X509Certificate;Ljava/util/List;Ljava/security/PrivateKey;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;", False, False)])
        setAuthPsk = JavaMethod("([B)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        addIkeSaProposal = JavaMethod("(Landroid/net/ipsec/ike/IkeSaProposal;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        removeIkeOption = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        addIkeOption = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setAuthEap = JavaMethod("(Ljava/security/cert/X509Certificate;Landroid/net/eap/EapSessionConfig;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setDpdDelaySeconds = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setLocalIdentification = JavaMethod("(Landroid/net/ipsec/ike/IkeIdentification;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setNattKeepAliveDelaySeconds = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setRemoteIdentification = JavaMethod("(Landroid/net/ipsec/ike/IkeIdentification;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setRetransmissionTimeoutsMillis = JavaMethod("([I)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setServerHostname = JavaMethod("(Ljava/lang/String;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        setNetwork = JavaMethod("(Landroid/net/Network;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams;")
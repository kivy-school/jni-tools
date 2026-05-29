from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ikev2VpnProfile"]

class Ikev2VpnProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Ikev2VpnProfile"
    TYPE_IKEV2_IPSEC_PSK = JavaStaticField("I")
    TYPE_IKEV2_IPSEC_RSA = JavaStaticField("I")
    TYPE_IKEV2_IPSEC_USER_PASS = JavaStaticField("I")
    getPassword = JavaMethod("()Ljava/lang/String;")
    getUsername = JavaMethod("()Ljava/lang/String;")
    isMetered = JavaMethod("()Z")
    getUserCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getServerAddr = JavaMethod("()Ljava/lang/String;")
    getRsaPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    getProxyInfo = JavaMethod("()Landroid/net/ProxyInfo;")
    getPresharedKey = JavaMethod("()[B")
    getAllowedAlgorithms = JavaMethod("()Ljava/util/List;")
    getIkeTunnelConnectionParams = JavaMethod("()Landroid/net/ipsec/ike/IkeTunnelConnectionParams;")
    getServerRootCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getUserIdentity = JavaMethod("()Ljava/lang/String;")
    isAutomaticIpVersionSelectionEnabled = JavaMethod("()Z")
    isAutomaticNattKeepaliveTimerEnabled = JavaMethod("()Z")
    isBypassable = JavaMethod("()Z")
    getMaxMtu = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/Ikev2VpnProfile$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/net/ipsec/ike/IkeTunnelConnectionParams;)V", False)]
        setMetered = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setMaxMtu = JavaMethod("(I)Landroid/net/Ikev2VpnProfile$Builder;")
        setAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/security/cert/X509Certificate;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAutomaticIpVersionSelectionEnabled = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setAutomaticNattKeepaliveTimerEnabled = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setBypassable = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setLocalRoutesExcluded = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setProxy = JavaMethod("(Landroid/net/ProxyInfo;)Landroid/net/Ikev2VpnProfile$Builder;")
        setRequiresInternetValidation = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setAllowedAlgorithms = JavaMethod("(Ljava/util/List;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAuthDigitalSignature = JavaMethod("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;Ljava/security/cert/X509Certificate;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAuthPsk = JavaMethod("([B)Landroid/net/Ikev2VpnProfile$Builder;")
        build = JavaMethod("()Landroid/net/Ikev2VpnProfile;")
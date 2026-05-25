from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ikev2VpnProfile"]

class Ikev2VpnProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Ikev2VpnProfile"
    getServerAddr = JavaMethod("()Ljava/lang/String;")
    getUserIdentity = JavaMethod("()Ljava/lang/String;")
    getPresharedKey = JavaMethod("()[B")
    getServerRootCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getUsername = JavaMethod("()Ljava/lang/String;")
    getPassword = JavaMethod("()Ljava/lang/String;")
    getRsaPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    getUserCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getProxyInfo = JavaMethod("()Landroid/net/ProxyInfo;")
    getAllowedAlgorithms = JavaMethod("()Ljava/util/List;")
    isBypassable = JavaMethod("()Z")
    isMetered = JavaMethod("()Z")
    getMaxMtu = JavaMethod("()I")
    getIkeTunnelConnectionParams = JavaMethod("()Landroid/net/ipsec/ike/IkeTunnelConnectionParams;")
    isAutomaticNattKeepaliveTimerEnabled = JavaMethod("()Z")
    isAutomaticIpVersionSelectionEnabled = JavaMethod("()Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/Ikev2VpnProfile/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/net/ipsec/ike/IkeTunnelConnectionParams;)V", False)]
        setAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/security/cert/X509Certificate;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAuthDigitalSignature = JavaMethod("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;Ljava/security/cert/X509Certificate;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAuthPsk = JavaMethod("([B)Landroid/net/Ikev2VpnProfile$Builder;")
        setBypassable = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setProxy = JavaMethod("(Landroid/net/ProxyInfo;)Landroid/net/Ikev2VpnProfile$Builder;")
        setMaxMtu = JavaMethod("(I)Landroid/net/Ikev2VpnProfile$Builder;")
        setRequiresInternetValidation = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setMetered = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setAllowedAlgorithms = JavaMethod("(Ljava/util/List;)Landroid/net/Ikev2VpnProfile$Builder;")
        setAutomaticNattKeepaliveTimerEnabled = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setAutomaticIpVersionSelectionEnabled = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        setLocalRoutesExcluded = JavaMethod("(Z)Landroid/net/Ikev2VpnProfile$Builder;")
        build = JavaMethod("()Landroid/net/Ikev2VpnProfile;")
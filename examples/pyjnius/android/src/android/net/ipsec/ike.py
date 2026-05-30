from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IkeSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionConfiguration"
    EXTENSION_TYPE_FRAGMENTATION = JavaStaticField("I")
    EXTENSION_TYPE_MOBIKE = JavaStaticField("I")
    getEapInfo = JavaMethod("()Landroid/net/eap/EapInfo;")
    getIkeSessionConnectionInfo = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConnectionInfo;")
    getRemoteApplicationVersion = JavaMethod("()Ljava/lang/String;")
    getRemoteVendorIds = JavaMethod("()Ljava/util/List;")
    isIkeExtensionEnabled = JavaMethod("(I)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionConfiguration$Builder"
        __javaconstructor__ = [("(Landroid/net/ipsec/ike/IkeSessionConnectionInfo;)V", False)]
        clearRemoteApplicationVersion = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        addIkeExtension = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        addRemoteVendorId = JavaMethod("([B)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        clearIkeExtensions = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        clearRemoteVendorIds = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        setEapInfo = JavaMethod("(Landroid/net/eap/EapInfo;)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        setRemoteApplicationVersion = JavaMethod("(Ljava/lang/String;)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration;")

class TunnelModeChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams"
    getConfigurationRequests = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class TunnelModeChildConfigRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$TunnelModeChildConfigRequest"

    class ConfigRequestIpv6DnsServer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv6DnsServer"

    class ConfigRequestIpv6Address(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv6Address"
        getPrefixLength = JavaMethod("()I")
        getAddress = JavaMethod("()Ljava/net/Inet6Address;")

    class ConfigRequestIpv4Netmask(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv4Netmask"

    class ConfigRequestIpv4DnsServer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv4DnsServer"

    class ConfigRequestIpv4DhcpServer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv4DhcpServer"

    class ConfigRequestIpv4Address(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$ConfigRequestIpv4Address"
        getAddress = JavaMethod("()Ljava/net/Inet4Address;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/net/ipsec/ike/TunnelModeChildSessionParams;)V", False)]
        addInternalDhcpServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalDnsServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addOutboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalAddressRequest = JavaMultipleMethod([("(Ljava/net/Inet6Address;I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(Ljava/net/Inet4Address;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False)])
        addChildSaProposal = JavaMethod("(Landroid/net/ipsec/ike/ChildSaProposal;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/TunnelModeChildSessionParams;")

class ChildSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionConfiguration"
    getInboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getOutboundTrafficSelectors = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/ChildSessionConfiguration$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/net/ipsec/ike/ChildSessionConfiguration;")

class TransportModeChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/TransportModeChildSessionParams"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TransportModeChildSessionParams$Builder"
        __javaconstructor__ = [("(Landroid/net/ipsec/ike/TransportModeChildSessionParams;)V", False), ("()V", False)]
        addOutboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        addChildSaProposal = JavaMethod("(Landroid/net/ipsec/ike/ChildSaProposal;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        addInboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/TransportModeChildSessionParams;")

class ChildSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionCallback"
    onIpSecTransformCreated = JavaMethod("(Landroid/net/IpSecTransform;I)V")
    onIpSecTransformDeleted = JavaMethod("(Landroid/net/IpSecTransform;I)V")
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onClosed = JavaMethod("()V")
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionConfiguration;)V")

class IkeTrafficSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeTrafficSelector"
    __javaconstructor__ = [("(IILjava/net/InetAddress;Ljava/net/InetAddress;)V", False)]
    endPort = JavaField("I")
    endingAddress = JavaField("Ljava/net/InetAddress;")
    startPort = JavaField("I")
    startingAddress = JavaField("Ljava/net/InetAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeFqdnIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeFqdnIdentification"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    fqdn = JavaField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeSessionConnectionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionConnectionInfo"
    __javaconstructor__ = [("(Ljava/net/InetAddress;Ljava/net/InetAddress;Landroid/net/Network;)V", False)]
    getNetwork = JavaMethod("()Landroid/net/Network;")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")

class IkeIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeIdentification"

class IkeSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionCallback"
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onError = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onClosed = JavaMethod("()V")
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/IkeSessionConfiguration;)V")

class IkeKeyIdIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeKeyIdIdentification"
    __javaconstructor__ = [("([B)V", False)]
    keyId = JavaField("[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSession"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/net/ipsec/ike/IkeSessionParams;Landroid/net/ipsec/ike/ChildSessionParams;Ljava/util/concurrent/Executor;Landroid/net/ipsec/ike/IkeSessionCallback;Landroid/net/ipsec/ike/ChildSessionCallback;)V", False)]
    kill = JavaMethod("()V")
    closeChildSession = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionCallback;)V")
    openChildSession = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionParams;Landroid/net/ipsec/ike/ChildSessionCallback;)V")
    finalize = JavaMethod("()V")
    close = JavaMethod("()V")
    dump = JavaMethod("(Ljava/io/PrintWriter;)V")

class IkeRfc822AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeRfc822AddrIdentification"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    rfc822Name = JavaField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeIpv4AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeIpv4AddrIdentification"
    __javaconstructor__ = [("(Ljava/net/Inet4Address;)V", False)]
    ipv4Address = JavaField("Ljava/net/Inet4Address;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class ChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionParams"
    getChildSaProposals = JavaMethod("()Ljava/util/List;")
    getInboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getHardLifetimeSeconds = JavaMethod("()I")
    getOutboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getSoftLifetimeSeconds = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class SaProposal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/SaProposal"
    DH_GROUP_1024_BIT_MODP = JavaStaticField("I")
    DH_GROUP_1536_BIT_MODP = JavaStaticField("I")
    DH_GROUP_2048_BIT_MODP = JavaStaticField("I")
    DH_GROUP_3072_BIT_MODP = JavaStaticField("I")
    DH_GROUP_4096_BIT_MODP = JavaStaticField("I")
    DH_GROUP_CURVE_25519 = JavaStaticField("I")
    DH_GROUP_NONE = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_3DES = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CBC = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CTR = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_12 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_16 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_8 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_CHACHA20_POLY1305 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_CMAC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_XCBC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA1_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_256_128 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_384_192 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_512_256 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_NONE = JavaStaticField("I")
    KEY_LEN_AES_128 = JavaStaticField("I")
    KEY_LEN_AES_192 = JavaStaticField("I")
    KEY_LEN_AES_256 = JavaStaticField("I")
    KEY_LEN_UNUSED = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_CMAC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_XCBC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_HMAC_SHA1 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_256 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_384 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_512 = JavaStaticField("I")
    getDhGroups = JavaMethod("()Ljava/util/List;")
    getEncryptionAlgorithms = JavaMethod("()Ljava/util/List;")
    getIntegrityAlgorithms = JavaMethod("()Ljava/util/List;")
    getSupportedDhGroups = JavaStaticMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

class IkeDerAsn1DnIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeDerAsn1DnIdentification"
    __javaconstructor__ = [("(Ljavax/security/auth/x500/X500Principal;)V", False)]
    derAsn1Dn = JavaField("Ljavax/security/auth/x500/X500Principal;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeTunnelConnectionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeTunnelConnectionParams"
    __javaconstructor__ = [("(Landroid/net/ipsec/ike/IkeSessionParams;Landroid/net/ipsec/ike/TunnelModeChildSessionParams;)V", False)]
    getIkeSessionParams = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams;")
    getTunnelModeChildSessionParams = JavaMethod("()Landroid/net/ipsec/ike/TunnelModeChildSessionParams;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class IkeSaProposal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSaProposal"
    DH_GROUP_1024_BIT_MODP = JavaStaticField("I")
    DH_GROUP_1536_BIT_MODP = JavaStaticField("I")
    DH_GROUP_2048_BIT_MODP = JavaStaticField("I")
    DH_GROUP_3072_BIT_MODP = JavaStaticField("I")
    DH_GROUP_4096_BIT_MODP = JavaStaticField("I")
    DH_GROUP_CURVE_25519 = JavaStaticField("I")
    DH_GROUP_NONE = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_3DES = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CBC = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CTR = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_12 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_16 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_8 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_CHACHA20_POLY1305 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_CMAC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_XCBC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA1_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_256_128 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_384_192 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_512_256 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_NONE = JavaStaticField("I")
    KEY_LEN_AES_128 = JavaStaticField("I")
    KEY_LEN_AES_192 = JavaStaticField("I")
    KEY_LEN_AES_256 = JavaStaticField("I")
    KEY_LEN_UNUSED = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_CMAC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_XCBC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_HMAC_SHA1 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_256 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_384 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_512 = JavaStaticField("I")
    getSupportedEncryptionAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getSupportedIntegrityAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getPseudorandomFunctions = JavaMethod("()Ljava/util/List;")
    getSupportedPseudorandomFunctions = JavaStaticMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSaProposal$Builder"
        __javaconstructor__ = [("()V", False)]
        addEncryptionAlgorithm = JavaMethod("(II)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addDhGroup = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addIntegrityAlgorithm = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        addPseudorandomFunction = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSaProposal$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSaProposal;")

class ChildSaProposal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSaProposal"
    DH_GROUP_1024_BIT_MODP = JavaStaticField("I")
    DH_GROUP_1536_BIT_MODP = JavaStaticField("I")
    DH_GROUP_2048_BIT_MODP = JavaStaticField("I")
    DH_GROUP_3072_BIT_MODP = JavaStaticField("I")
    DH_GROUP_4096_BIT_MODP = JavaStaticField("I")
    DH_GROUP_CURVE_25519 = JavaStaticField("I")
    DH_GROUP_NONE = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_3DES = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CBC = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_CTR = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_12 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_16 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_AES_GCM_8 = JavaStaticField("I")
    ENCRYPTION_ALGORITHM_CHACHA20_POLY1305 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_CMAC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_AES_XCBC_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA1_96 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_256_128 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_384_192 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_HMAC_SHA2_512_256 = JavaStaticField("I")
    INTEGRITY_ALGORITHM_NONE = JavaStaticField("I")
    KEY_LEN_AES_128 = JavaStaticField("I")
    KEY_LEN_AES_192 = JavaStaticField("I")
    KEY_LEN_AES_256 = JavaStaticField("I")
    KEY_LEN_UNUSED = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_CMAC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_AES128_XCBC = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_HMAC_SHA1 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_256 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_384 = JavaStaticField("I")
    PSEUDORANDOM_FUNCTION_SHA2_512 = JavaStaticField("I")
    getSupportedEncryptionAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getSupportedIntegrityAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/ChildSaProposal$Builder"
        __javaconstructor__ = [("()V", False)]
        addEncryptionAlgorithm = JavaMethod("(II)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        addDhGroup = JavaMethod("(I)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        addIntegrityAlgorithm = JavaMethod("(I)Landroid/net/ipsec/ike/ChildSaProposal$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/ChildSaProposal;")

class IkeIpv6AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeIpv6AddrIdentification"
    __javaconstructor__ = [("(Ljava/net/Inet6Address;)V", False)]
    ipv6Address = JavaField("Ljava/net/Inet6Address;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

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
        __javaconstructor__ = [("()V", False), ("(Landroid/net/ipsec/ike/IkeSessionParams;)V", False)]
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
        setAuthDigitalSignature = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;Ljava/security/cert/X509Certificate;Ljava/util/List;Ljava/security/PrivateKey;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;", False, False), ("(Ljava/security/cert/X509Certificate;Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;)Landroid/net/ipsec/ike/IkeSessionParams$Builder;", False, False)])
        setAuthPsk = JavaMethod("([B)Landroid/net/ipsec/ike/IkeSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TunnelModeChildSessionParams"]

class TunnelModeChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams"
    getConfigurationRequests = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/net/ipsec/ike/TunnelModeChildSessionParams;)V", False)]
        addChildSaProposal = JavaMethod("(Landroid/net/ipsec/ike/ChildSaProposal;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addOutboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalAddressRequest = JavaMultipleMethod([("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(Ljava/net/Inet4Address;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(Ljava/net/Inet6Address;I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False)])
        addInternalDnsServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalDhcpServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/TunnelModeChildSessionParams;")

    class ConfigRequestIpv4Address(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv4Address"
        getAddress = JavaMethod("()Ljava/net/Inet4Address;")

    class ConfigRequestIpv4DhcpServer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv4DhcpServer"

    class ConfigRequestIpv4DnsServer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv4DnsServer"

    class ConfigRequestIpv4Netmask(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv4Netmask"

    class ConfigRequestIpv6Address(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv6Address"
        getAddress = JavaMethod("()Ljava/net/Inet6Address;")
        getPrefixLength = JavaMethod("()I")

    class ConfigRequestIpv6DnsServer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/ConfigRequestIpv6DnsServer"

    class TunnelModeChildConfigRequest(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TunnelModeChildSessionParams/TunnelModeChildConfigRequest"
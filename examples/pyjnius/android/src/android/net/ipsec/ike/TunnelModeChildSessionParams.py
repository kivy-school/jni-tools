from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TunnelModeChildSessionParams"]

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
        getAddress = JavaMethod("()Ljava/net/Inet6Address;")
        getPrefixLength = JavaMethod("()I")

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
        addChildSaProposal = JavaMethod("(Landroid/net/ipsec/ike/ChildSaProposal;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalAddressRequest = JavaMultipleMethod([("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(Ljava/net/Inet4Address;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False), ("(Ljava/net/Inet6Address;I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;", False, False)])
        addInternalDhcpServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addInternalDnsServerRequest = JavaMethod("(I)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        addOutboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/TunnelModeChildSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/TunnelModeChildSessionParams;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnGatewayConnectionConfig"]

class VcnGatewayConnectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnGatewayConnectionConfig"
    MIN_UDP_PORT_4500_NAT_TIMEOUT_UNSET = JavaStaticField("I")
    VCN_GATEWAY_OPTION_ENABLE_DATA_STALL_RECOVERY_WITH_MOBILITY = JavaStaticField("I")
    getMaxMtu = JavaMethod("()I")
    getExposedCapabilities = JavaMethod("()[I")
    getGatewayConnectionName = JavaMethod("()Ljava/lang/String;")
    getMinUdpPort4500NatTimeoutSeconds = JavaMethod("()I")
    getRetryIntervalsMillis = JavaMethod("()[J")
    getVcnUnderlyingNetworkPriorities = JavaMethod("()Ljava/util/List;")
    hasGatewayOption = JavaMethod("(I)Z")
    isSafeModeEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnGatewayConnectionConfig$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/net/ipsec/ike/IkeTunnelConnectionParams;)V", False)]
        addGatewayOption = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setMaxMtu = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        addExposedCapability = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        removeExposedCapability = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        removeGatewayOption = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setMinUdpPort4500NatTimeoutSeconds = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setRetryIntervalsMillis = JavaMethod("([J)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setSafeModeEnabled = JavaMethod("(Z)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setVcnUnderlyingNetworkPriorities = JavaMethod("(Ljava/util/List;)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnGatewayConnectionConfig;")
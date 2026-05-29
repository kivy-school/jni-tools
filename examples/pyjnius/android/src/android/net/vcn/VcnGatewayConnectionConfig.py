from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnGatewayConnectionConfig"]

class VcnGatewayConnectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnGatewayConnectionConfig"
    VCN_GATEWAY_OPTION_ENABLE_DATA_STALL_RECOVERY_WITH_MOBILITY = JavaStaticField("I")
    getGatewayConnectionName = JavaMethod("()Ljava/lang/String;")
    getExposedCapabilities = JavaMethod("()[I")
    getVcnUnderlyingNetworkPriorities = JavaMethod("()Ljava/util/List;")
    getRetryIntervalsMillis = JavaMethod("()[J")
    getMaxMtu = JavaMethod("()I")
    getMinUdpPort4500NatTimeoutSeconds = JavaMethod("()I")
    isSafeModeEnabled = JavaMethod("()Z")
    hasGatewayOption = JavaMethod("(I)Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnGatewayConnectionConfig/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/net/ipsec/ike/IkeTunnelConnectionParams;)V", False)]
        addExposedCapability = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        removeExposedCapability = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setVcnUnderlyingNetworkPriorities = JavaMethod("(Ljava/util/List;)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setRetryIntervalsMillis = JavaMethod("([J)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setMaxMtu = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setMinUdpPort4500NatTimeoutSeconds = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        addGatewayOption = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        removeGatewayOption = JavaMethod("(I)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        setSafeModeEnabled = JavaMethod("(Z)Landroid/net/vcn/VcnGatewayConnectionConfig$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnGatewayConnectionConfig;")
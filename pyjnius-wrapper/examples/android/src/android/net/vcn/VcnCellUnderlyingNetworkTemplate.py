from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnCellUnderlyingNetworkTemplate"]

class VcnCellUnderlyingNetworkTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnCellUnderlyingNetworkTemplate"
    getOperatorPlmnIds = JavaMethod("()Ljava/util/Set;")
    getSimSpecificCarrierIds = JavaMethod("()Ljava/util/Set;")
    getRoaming = JavaMethod("()I")
    getOpportunistic = JavaMethod("()I")
    getCbs = JavaMethod("()I")
    getDun = JavaMethod("()I")
    getIms = JavaMethod("()I")
    getInternet = JavaMethod("()I")
    getMms = JavaMethod("()I")
    getRcs = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnCellUnderlyingNetworkTemplate/Builder"
        __javaconstructor__ = [("()V", False)]
        setMetered = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setOperatorPlmnIds = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setSimSpecificCarrierIds = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setRoaming = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setOpportunistic = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMinUpstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMinDownstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setCbs = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setDun = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setIms = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setInternet = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMms = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setRcs = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate;")
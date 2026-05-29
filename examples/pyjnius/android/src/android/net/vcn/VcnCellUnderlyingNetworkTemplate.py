from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnCellUnderlyingNetworkTemplate"]

class VcnCellUnderlyingNetworkTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnCellUnderlyingNetworkTemplate"
    MATCH_ANY = JavaStaticField("I")
    MATCH_FORBIDDEN = JavaStaticField("I")
    MATCH_REQUIRED = JavaStaticField("I")
    getRoaming = JavaMethod("()I")
    getMms = JavaMethod("()I")
    getOpportunistic = JavaMethod("()I")
    getOperatorPlmnIds = JavaMethod("()Ljava/util/Set;")
    getRcs = JavaMethod("()I")
    getDun = JavaMethod("()I")
    getCbs = JavaMethod("()I")
    getInternet = JavaMethod("()I")
    getIms = JavaMethod("()I")
    getSimSpecificCarrierIds = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder"
        __javaconstructor__ = [("()V", False)]
        setRoaming = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMetered = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setDun = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setIms = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setCbs = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMms = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setOperatorPlmnIds = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setRcs = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setSimSpecificCarrierIds = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setInternet = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMinDownstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        setMinUpstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate;")
        setOpportunistic = JavaMethod("(I)Landroid/net/vcn/VcnCellUnderlyingNetworkTemplate$Builder;")
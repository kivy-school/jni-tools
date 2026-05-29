from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnWifiUnderlyingNetworkTemplate"]

class VcnWifiUnderlyingNetworkTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnWifiUnderlyingNetworkTemplate"
    MATCH_ANY = JavaStaticField("I")
    MATCH_FORBIDDEN = JavaStaticField("I")
    MATCH_REQUIRED = JavaStaticField("I")
    getSsids = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnWifiUnderlyingNetworkTemplate$Builder"
        __javaconstructor__ = [("()V", False)]
        setMetered = JavaMethod("(I)Landroid/net/vcn/VcnWifiUnderlyingNetworkTemplate$Builder;")
        setSsids = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnWifiUnderlyingNetworkTemplate$Builder;")
        setMinDownstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnWifiUnderlyingNetworkTemplate$Builder;")
        setMinUpstreamBandwidthKbps = JavaMethod("(II)Landroid/net/vcn/VcnWifiUnderlyingNetworkTemplate$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnWifiUnderlyingNetworkTemplate;")
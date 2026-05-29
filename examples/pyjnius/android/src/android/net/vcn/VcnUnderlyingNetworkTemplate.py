from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnUnderlyingNetworkTemplate"]

class VcnUnderlyingNetworkTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnUnderlyingNetworkTemplate"
    MATCH_ANY = JavaStaticField("I")
    MATCH_FORBIDDEN = JavaStaticField("I")
    MATCH_REQUIRED = JavaStaticField("I")
    getMetered = JavaMethod("()I")
    getMinEntryDownstreamBandwidthKbps = JavaMethod("()I")
    getMinEntryUpstreamBandwidthKbps = JavaMethod("()I")
    getMinExitDownstreamBandwidthKbps = JavaMethod("()I")
    getMinExitUpstreamBandwidthKbps = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
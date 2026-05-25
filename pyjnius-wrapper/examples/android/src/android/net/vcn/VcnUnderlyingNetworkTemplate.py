from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnUnderlyingNetworkTemplate"]

class VcnUnderlyingNetworkTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnUnderlyingNetworkTemplate"
    MATCH_ANY = JavaStaticField("I")
    MATCH_FORBIDDEN = JavaStaticField("I")
    MATCH_REQUIRED = JavaStaticField("I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getMetered = JavaMethod("()I")
    getMinEntryUpstreamBandwidthKbps = JavaMethod("()I")
    getMinExitUpstreamBandwidthKbps = JavaMethod("()I")
    getMinEntryDownstreamBandwidthKbps = JavaMethod("()I")
    getMinExitDownstreamBandwidthKbps = JavaMethod("()I")
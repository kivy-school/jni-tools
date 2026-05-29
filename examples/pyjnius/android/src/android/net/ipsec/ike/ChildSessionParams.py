from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSessionParams"]

class ChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionParams"
    getChildSaProposals = JavaMethod("()Ljava/util/List;")
    getHardLifetimeSeconds = JavaMethod("()I")
    getInboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getOutboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getSoftLifetimeSeconds = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
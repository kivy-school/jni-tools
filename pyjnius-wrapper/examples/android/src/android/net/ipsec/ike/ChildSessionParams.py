from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSessionParams"]

class ChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionParams"
    getInboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getOutboundTrafficSelectors = JavaMethod("()Ljava/util/List;")
    getChildSaProposals = JavaMethod("()Ljava/util/List;")
    getHardLifetimeSeconds = JavaMethod("()I")
    getSoftLifetimeSeconds = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
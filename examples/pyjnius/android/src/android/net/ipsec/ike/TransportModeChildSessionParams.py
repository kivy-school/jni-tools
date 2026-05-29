from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportModeChildSessionParams"]

class TransportModeChildSessionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/TransportModeChildSessionParams"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/TransportModeChildSessionParams$Builder"
        __javaconstructor__ = [("(Landroid/net/ipsec/ike/TransportModeChildSessionParams;)V", False), ("()V", False)]
        addChildSaProposal = JavaMethod("(Landroid/net/ipsec/ike/ChildSaProposal;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        addInboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        addOutboundTrafficSelectors = JavaMethod("(Landroid/net/ipsec/ike/IkeTrafficSelector;)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        setLifetimeSeconds = JavaMethod("(II)Landroid/net/ipsec/ike/TransportModeChildSessionParams$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/TransportModeChildSessionParams;")
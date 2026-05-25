from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeTunnelConnectionParams"]

class IkeTunnelConnectionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeTunnelConnectionParams"
    __javaconstructor__ = [("(Landroid/net/ipsec/ike/IkeSessionParams;Landroid/net/ipsec/ike/TunnelModeChildSessionParams;)V", False)]
    getIkeSessionParams = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionParams;")
    getTunnelModeChildSessionParams = JavaMethod("()Landroid/net/ipsec/ike/TunnelModeChildSessionParams;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
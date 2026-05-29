from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionConnectionInfo"]

class IkeSessionConnectionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionConnectionInfo"
    __javaconstructor__ = [("(Ljava/net/InetAddress;Ljava/net/InetAddress;Landroid/net/Network;)V", False)]
    getNetwork = JavaMethod("()Landroid/net/Network;")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")
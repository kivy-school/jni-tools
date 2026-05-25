from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionConnectionInfo"]

class IkeSessionConnectionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionConnectionInfo"
    __javaconstructor__ = [("(Ljava/net/InetAddress;Ljava/net/InetAddress;Landroid/net/Network;)V", False)]
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getNetwork = JavaMethod("()Landroid/net/Network;")
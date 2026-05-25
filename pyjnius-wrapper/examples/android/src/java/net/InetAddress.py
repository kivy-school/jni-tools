from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InetAddress"]

class InetAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/InetAddress"
    isMulticastAddress = JavaMethod("()Z")
    isAnyLocalAddress = JavaMethod("()Z")
    isLoopbackAddress = JavaMethod("()Z")
    isLinkLocalAddress = JavaMethod("()Z")
    isSiteLocalAddress = JavaMethod("()Z")
    isMCGlobal = JavaMethod("()Z")
    isMCNodeLocal = JavaMethod("()Z")
    isMCLinkLocal = JavaMethod("()Z")
    isMCSiteLocal = JavaMethod("()Z")
    isMCOrgLocal = JavaMethod("()Z")
    isReachable = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/net/NetworkInterface;II)Z", False, False)])
    getHostName = JavaMethod("()Ljava/lang/String;")
    getCanonicalHostName = JavaMethod("()Ljava/lang/String;")
    getAddress = JavaMethod("()[B")
    getHostAddress = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getByAddress = JavaMultipleMethod([("(Ljava/lang/String;[B)Ljava/net/InetAddress;", True, False), ("([B)Ljava/net/InetAddress;", True, False)])
    getByName = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")
    getAllByName = JavaStaticMethod("(Ljava/lang/String;)[Ljava/net/InetAddress;")
    getLoopbackAddress = JavaStaticMethod("()Ljava/net/InetAddress;")
    getLocalHost = JavaStaticMethod("()Ljava/net/InetAddress;")
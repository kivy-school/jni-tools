from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inet6Address"]

class Inet6Address(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Inet6Address"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()[B")
    getHostAddress = JavaMethod("()Ljava/lang/String;")
    ofLiteral = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")
    getByAddress = JavaMultipleMethod([("(Ljava/lang/String;[BLjava/net/NetworkInterface;)Ljava/net/Inet6Address;", True, False), ("(Ljava/lang/String;[BI)Ljava/net/Inet6Address;", True, False)])
    isMulticastAddress = JavaMethod("()Z")
    isAnyLocalAddress = JavaMethod("()Z")
    isLoopbackAddress = JavaMethod("()Z")
    isSiteLocalAddress = JavaMethod("()Z")
    isMCGlobal = JavaMethod("()Z")
    isMCNodeLocal = JavaMethod("()Z")
    isMCLinkLocal = JavaMethod("()Z")
    isMCSiteLocal = JavaMethod("()Z")
    isMCOrgLocal = JavaMethod("()Z")
    isIPv4CompatibleAddress = JavaMethod("()Z")
    getScopedInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    isLinkLocalAddress = JavaMethod("()Z")
    getScopeId = JavaMethod("()I")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inet6Address"]

class Inet6Address(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Inet6Address"
    getByAddress = JavaMultipleMethod([("(Ljava/lang/String;[BLjava/net/NetworkInterface;)Ljava/net/Inet6Address;", True, False), ("(Ljava/lang/String;[BI)Ljava/net/Inet6Address;", True, False)])
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
    getAddress = JavaMethod("()[B")
    getScopeId = JavaMethod("()I")
    getScopedInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    getHostAddress = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    isIPv4CompatibleAddress = JavaMethod("()Z")
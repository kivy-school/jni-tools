from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inet4Address"]

class Inet4Address(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Inet4Address"
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
    getHostAddress = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
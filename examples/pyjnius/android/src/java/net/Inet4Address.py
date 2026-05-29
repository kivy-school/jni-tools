from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inet4Address"]

class Inet4Address(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Inet4Address"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()[B")
    getHostAddress = JavaMethod("()Ljava/lang/String;")
    ofLiteral = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/Inet4Address;")
    isMulticastAddress = JavaMethod("()Z")
    isAnyLocalAddress = JavaMethod("()Z")
    isLoopbackAddress = JavaMethod("()Z")
    isSiteLocalAddress = JavaMethod("()Z")
    isMCGlobal = JavaMethod("()Z")
    isMCNodeLocal = JavaMethod("()Z")
    isMCLinkLocal = JavaMethod("()Z")
    isMCSiteLocal = JavaMethod("()Z")
    isMCOrgLocal = JavaMethod("()Z")
    ofPosixLiteral = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/Inet4Address;")
    isLinkLocalAddress = JavaMethod("()Z")
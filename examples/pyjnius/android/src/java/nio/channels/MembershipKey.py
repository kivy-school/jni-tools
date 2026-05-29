from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MembershipKey"]

class MembershipKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MembershipKey"
    sourceAddress = JavaMethod("()Ljava/net/InetAddress;")
    group = JavaMethod("()Ljava/net/InetAddress;")
    unblock = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
    isValid = JavaMethod("()Z")
    channel = JavaMethod("()Ljava/nio/channels/MulticastChannel;")
    networkInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    drop = JavaMethod("()V")
    block = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
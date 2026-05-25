from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MembershipKey"]

class MembershipKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MembershipKey"
    __javaconstructor__ = [("()V", False)]
    isValid = JavaMethod("()Z")
    drop = JavaMethod("()V")
    block = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
    unblock = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
    channel = JavaMethod("()Ljava/nio/channels/MulticastChannel;")
    group = JavaMethod("()Ljava/net/InetAddress;")
    networkInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    sourceAddress = JavaMethod("()Ljava/net/InetAddress;")
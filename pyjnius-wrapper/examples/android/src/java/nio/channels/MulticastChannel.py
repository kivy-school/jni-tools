from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MulticastChannel"]

class MulticastChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MulticastChannel"
    close = JavaMethod("()V")
    join = JavaMultipleMethod([("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;)Ljava/nio/channels/MembershipKey;", False, False), ("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;", False, False)])
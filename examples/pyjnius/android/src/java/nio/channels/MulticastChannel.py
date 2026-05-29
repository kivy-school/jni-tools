from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MulticastChannel"]

class MulticastChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MulticastChannel"
    join = JavaMultipleMethod([("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;)Ljava/nio/channels/MembershipKey;", False, False), ("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;", False, False)])
    close = JavaMethod("()V")
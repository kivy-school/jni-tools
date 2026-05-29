from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MulticastSocket"]

class MulticastSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/MulticastSocket"
    __javaconstructor__ = [("(Ljava/net/SocketAddress;)V", False), ("(I)V", False), ("()V", False)]
    setInterface = JavaMethod("(Ljava/net/InetAddress;)V")
    setTimeToLive = JavaMethod("(I)V")
    getInterface = JavaMethod("()Ljava/net/InetAddress;")
    setNetworkInterface = JavaMethod("(Ljava/net/NetworkInterface;)V")
    getNetworkInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    setLoopbackMode = JavaMethod("(Z)V")
    getLoopbackMode = JavaMethod("()Z")
    getTimeToLive = JavaMethod("()I")
    joinGroup = JavaMultipleMethod([("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V", False, False), ("(Ljava/net/InetAddress;)V", False, False)])
    leaveGroup = JavaMultipleMethod([("(Ljava/net/InetAddress;)V", False, False), ("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V", False, False)])
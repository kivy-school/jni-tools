from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MulticastSocket"]

class MulticastSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/MulticastSocket"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/net/SocketAddress;)V", False)]
    setTTL = JavaMethod("(B)V")
    setTimeToLive = JavaMethod("(I)V")
    getTTL = JavaMethod("()B")
    getTimeToLive = JavaMethod("()I")
    joinGroup = JavaMultipleMethod([("(Ljava/net/InetAddress;)V", False, False), ("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V", False, False)])
    leaveGroup = JavaMultipleMethod([("(Ljava/net/InetAddress;)V", False, False), ("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V", False, False)])
    setInterface = JavaMethod("(Ljava/net/InetAddress;)V")
    getInterface = JavaMethod("()Ljava/net/InetAddress;")
    setNetworkInterface = JavaMethod("(Ljava/net/NetworkInterface;)V")
    getNetworkInterface = JavaMethod("()Ljava/net/NetworkInterface;")
    setLoopbackMode = JavaMethod("(Z)V")
    getLoopbackMode = JavaMethod("()Z")
    send = JavaMethod("(Ljava/net/DatagramPacket;B)V")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
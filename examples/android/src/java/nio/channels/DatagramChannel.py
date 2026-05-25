from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramChannel"]

class DatagramChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/DatagramChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
    open = JavaMultipleMethod([("()Ljava/nio/channels/DatagramChannel;", True, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", True, False)])
    validOps = JavaMethod("()I")
    bind = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/DatagramChannel;")
    socket = JavaMethod("()Ljava/net/DatagramSocket;")
    isConnected = JavaMethod("()Z")
    connect = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;")
    disconnect = JavaMethod("()Ljava/nio/channels/DatagramChannel;")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    receive = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/net/SocketAddress;")
    send = JavaMethod("(Ljava/nio/ByteBuffer;Ljava/net/SocketAddress;)I")
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
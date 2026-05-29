from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramChannel"]

class DatagramChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/DatagramChannel"
    connect = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;")
    isConnected = JavaMethod("()Z")
    disconnect = JavaMethod("()Ljava/nio/channels/DatagramChannel;")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    write = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;)J", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    open = JavaMultipleMethod([("()Ljava/nio/channels/DatagramChannel;", True, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", True, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    send = JavaMethod("(Ljava/nio/ByteBuffer;Ljava/net/SocketAddress;)I")
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;", False, False)])
    validOps = JavaMethod("()I")
    socket = JavaMethod("()Ljava/net/DatagramSocket;")
    receive = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/net/SocketAddress;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/DatagramChannel;", False, False)])
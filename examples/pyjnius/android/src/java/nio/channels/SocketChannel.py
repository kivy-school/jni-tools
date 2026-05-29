from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketChannel"]

class SocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SocketChannel"
    connect = JavaMethod("(Ljava/net/SocketAddress;)Z")
    isConnected = JavaMethod("()Z")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    open = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;", True, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/SocketChannel;", True, False), ("()Ljava/nio/channels/SocketChannel;", True, False)])
    read = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False)])
    isConnectionPending = JavaMethod("()Z")
    finishConnect = JavaMethod("()Z")
    validOps = JavaMethod("()I")
    socket = JavaMethod("()Ljava/net/Socket;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/SocketChannel;", False, False)])
    shutdownInput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
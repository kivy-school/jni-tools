from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketChannel"]

class SocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SocketChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
    open = JavaMultipleMethod([("()Ljava/nio/channels/SocketChannel;", True, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;", True, False)])
    validOps = JavaMethod("()I")
    bind = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/SocketChannel;")
    shutdownInput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    socket = JavaMethod("()Ljava/net/Socket;")
    isConnected = JavaMethod("()Z")
    isConnectionPending = JavaMethod("()Z")
    connect = JavaMethod("(Ljava/net/SocketAddress;)Z")
    finishConnect = JavaMethod("()Z")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
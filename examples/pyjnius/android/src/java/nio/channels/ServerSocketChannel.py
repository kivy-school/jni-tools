from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocketChannel"]

class ServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ServerSocketChannel"
    accept = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    open = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/ServerSocketChannel;", True, False), ("()Ljava/nio/channels/ServerSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;I)Ljava/nio/channels/ServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/ServerSocketChannel;", False, False)])
    validOps = JavaMethod("()I")
    socket = JavaMethod("()Ljava/net/ServerSocket;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/ServerSocketChannel;", False, False)])
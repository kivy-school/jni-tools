from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocketChannel"]

class ServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ServerSocketChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
    open = JavaStaticMethod("()Ljava/nio/channels/ServerSocketChannel;")
    validOps = JavaMethod("()I")
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/ServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;I)Ljava/nio/channels/ServerSocketChannel;", False, False)])
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/ServerSocketChannel;")
    socket = JavaMethod("()Ljava/net/ServerSocket;")
    accept = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousServerSocketChannel"]

class AsynchronousServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousServerSocketChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/AsynchronousChannelProvider;)V", False)]
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    open = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False), ("()Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;I)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False)])
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousServerSocketChannel;")
    accept = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("()Ljava/util/concurrent/Future;", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
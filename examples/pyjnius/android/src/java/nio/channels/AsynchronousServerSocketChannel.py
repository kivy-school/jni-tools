from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousServerSocketChannel"]

class AsynchronousServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousServerSocketChannel"
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    accept = JavaMultipleMethod([("()Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    open = JavaMultipleMethod([("()Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False), ("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;I)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False)])
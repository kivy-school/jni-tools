from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousSocketChannel"]

class AsynchronousSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousSocketChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/AsynchronousChannelProvider;)V", False)]
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    open = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;", True, False), ("()Ljava/nio/channels/AsynchronousSocketChannel;", True, False)])
    bind = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousSocketChannel;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousSocketChannel;")
    shutdownInput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    connect = JavaMultipleMethod([("(Ljava/net/SocketAddress;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/net/SocketAddress;)Ljava/util/concurrent/Future;", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
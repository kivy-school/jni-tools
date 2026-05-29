from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousSocketChannel"]

class AsynchronousSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousSocketChannel"
    connect = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/net/SocketAddress;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    open = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;", True, False), ("()Ljava/nio/channels/AsynchronousSocketChannel;", True, False)])
    read = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousSocketChannel;", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousSocketChannel;", False, False)])
    shutdownInput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")
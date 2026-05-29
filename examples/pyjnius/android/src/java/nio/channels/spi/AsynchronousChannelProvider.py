from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousChannelProvider"]

class AsynchronousChannelProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AsynchronousChannelProvider"
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    openAsynchronousSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;")
    openAsynchronousChannelGroup = JavaMultipleMethod([("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;", False, False), ("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;", False, False)])
    openAsynchronousServerSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousChannelProvider"]

class AsynchronousChannelProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AsynchronousChannelProvider"
    __javaconstructor__ = [("()V", False)]
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    openAsynchronousChannelGroup = JavaMultipleMethod([("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;", False, False), ("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;", False, False)])
    openAsynchronousServerSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;")
    openAsynchronousSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;")
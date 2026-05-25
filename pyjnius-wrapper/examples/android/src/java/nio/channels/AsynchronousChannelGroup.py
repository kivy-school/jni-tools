from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousChannelGroup"]

class AsynchronousChannelGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousChannelGroup"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/AsynchronousChannelProvider;)V", False)]
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    withFixedThreadPool = JavaStaticMethod("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;")
    withCachedThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;")
    withThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;)Ljava/nio/channels/AsynchronousChannelGroup;")
    isShutdown = JavaMethod("()Z")
    isTerminated = JavaMethod("()Z")
    shutdown = JavaMethod("()V")
    shutdownNow = JavaMethod("()V")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
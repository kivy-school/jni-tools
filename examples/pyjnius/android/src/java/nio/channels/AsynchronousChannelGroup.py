from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousChannelGroup"]

class AsynchronousChannelGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousChannelGroup"
    shutdown = JavaMethod("()V")
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    isTerminated = JavaMethod("()Z")
    isShutdown = JavaMethod("()Z")
    withFixedThreadPool = JavaStaticMethod("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;")
    withCachedThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;")
    withThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;)Ljava/nio/channels/AsynchronousChannelGroup;")
    shutdownNow = JavaMethod("()V")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
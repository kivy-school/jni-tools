from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AsynchronousChannelProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AsynchronousChannelProvider"
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    openAsynchronousSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;")
    openAsynchronousChannelGroup = JavaMultipleMethod([("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;", False, False), ("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;", False, False)])
    openAsynchronousServerSocketChannel = JavaMethod("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;")

class AbstractSelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectableChannel"
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    isBlocking = JavaMethod("()Z")
    isRegistered = JavaMethod("()Z")
    register = JavaMethod("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")

class AbstractSelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectionKey"
    OP_READ = JavaStaticField("I")
    OP_WRITE = JavaStaticField("I")
    OP_CONNECT = JavaStaticField("I")
    OP_ACCEPT = JavaStaticField("I")
    cancel = JavaMethod("()V")
    isValid = JavaMethod("()Z")

class SelectorProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/SelectorProvider"
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    inheritedChannel = JavaMethod("()Ljava/nio/channels/Channel;")
    openSelector = JavaMethod("()Ljava/nio/channels/spi/AbstractSelector;")
    openPipe = JavaMethod("()Ljava/nio/channels/Pipe;")
    openSocketChannel = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/SocketChannel;", False, False), ("()Ljava/nio/channels/SocketChannel;", False, False)])
    openServerSocketChannel = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/ServerSocketChannel;", False, False), ("()Ljava/nio/channels/ServerSocketChannel;", False, False)])
    openDatagramChannel = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", False, False), ("()Ljava/nio/channels/DatagramChannel;", False, False)])

class AbstractInterruptibleChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractInterruptibleChannel"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")

class AbstractSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelector"
    isOpen = JavaMethod("()Z")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    close = JavaMethod("()V")
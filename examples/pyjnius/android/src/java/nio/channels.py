from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CompletionHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/CompletionHandler"
    completed = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    failed = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/Object;)V")

class CancelledKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/CancelledKeyException"
    __javaconstructor__ = [("()V", False)]

class AsynchronousSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousSocketChannel"
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("([Ljava/nio/ByteBuffer;IIJLjava/util/concurrent/TimeUnit;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False)])
    connect = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/net/SocketAddress;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    open = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousSocketChannel;", True, False), ("()Ljava/nio/channels/AsynchronousSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousSocketChannel;", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousSocketChannel;", False, False)])
    shutdownInput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/AsynchronousSocketChannel;")

class SelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectableChannel"
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    isBlocking = JavaMethod("()Z")
    isRegistered = JavaMethod("()Z")
    register = JavaMultipleMethod([("(Ljava/nio/channels/Selector;I)Ljava/nio/channels/SelectionKey;", False, False), ("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;", False, False)])
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")
    validOps = JavaMethod("()I")

class Channel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Channel"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")

class DatagramChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/DatagramChannel"
    isConnected = JavaMethod("()Z")
    disconnect = JavaMethod("()Ljava/nio/channels/DatagramChannel;")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    write = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    connect = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;")
    open = JavaMultipleMethod([("()Ljava/nio/channels/DatagramChannel;", True, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", True, False)])
    send = JavaMethod("(Ljava/nio/ByteBuffer;Ljava/net/SocketAddress;)I")
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/DatagramChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False)])
    socket = JavaMethod("()Ljava/net/DatagramSocket;")
    receive = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/net/SocketAddress;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/DatagramChannel;", False, False)])
    validOps = JavaMethod("()I")

class ByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ByteChannel"

class NoConnectionPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NoConnectionPendingException"
    __javaconstructor__ = [("()V", False)]

class Pipe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Pipe"
    sink = JavaMethod("()Ljava/nio/channels/Pipe$SinkChannel;")
    source = JavaMethod("()Ljava/nio/channels/Pipe$SourceChannel;")
    open = JavaStaticMethod("()Ljava/nio/channels/Pipe;")

    class SinkChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe$SinkChannel"
        validOps = JavaMethod("()I")

    class SourceChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe$SourceChannel"
        validOps = JavaMethod("()I")

class IllegalSelectorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalSelectorException"
    __javaconstructor__ = [("()V", False)]

class UnresolvedAddressException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/UnresolvedAddressException"
    __javaconstructor__ = [("()V", False)]

class NonWritableChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NonWritableChannelException"
    __javaconstructor__ = [("()V", False)]

class MembershipKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MembershipKey"
    unblock = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
    sourceAddress = JavaMethod("()Ljava/net/InetAddress;")
    drop = JavaMethod("()V")
    group = JavaMethod("()Ljava/net/InetAddress;")
    block = JavaMethod("(Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;")
    channel = JavaMethod("()Ljava/nio/channels/MulticastChannel;")
    isValid = JavaMethod("()Z")
    networkInterface = JavaMethod("()Ljava/net/NetworkInterface;")

class AsynchronousChannelGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousChannelGroup"
    shutdown = JavaMethod("()V")
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    isTerminated = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    shutdownNow = JavaMethod("()V")
    isShutdown = JavaMethod("()Z")
    withFixedThreadPool = JavaStaticMethod("(ILjava/util/concurrent/ThreadFactory;)Ljava/nio/channels/AsynchronousChannelGroup;")
    withCachedThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;I)Ljava/nio/channels/AsynchronousChannelGroup;")
    withThreadPool = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;)Ljava/nio/channels/AsynchronousChannelGroup;")

class GatheringByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/GatheringByteChannel"
    write = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])

class InterruptedByTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/InterruptedByTimeoutException"
    __javaconstructor__ = [("()V", False)]

class NotYetConnectedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NotYetConnectedException"
    __javaconstructor__ = [("()V", False)]

class SocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SocketChannel"
    isConnected = JavaMethod("()Z")
    getRemoteAddress = JavaMethod("()Ljava/net/SocketAddress;")
    write = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    read = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    connect = JavaMethod("(Ljava/net/SocketAddress;)Z")
    open = JavaMultipleMethod([("()Ljava/nio/channels/SocketChannel;", True, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/SocketChannel;", True, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/SocketChannel;", False, False)])
    socket = JavaMethod("()Ljava/net/Socket;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/SocketChannel;", False, False)])
    shutdownInput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    shutdownOutput = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    isConnectionPending = JavaMethod("()Z")
    finishConnect = JavaMethod("()Z")
    validOps = JavaMethod("()I")

class NetworkChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NetworkChannel"
    bind = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")

class OverlappingFileLockException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/OverlappingFileLockException"
    __javaconstructor__ = [("()V", False)]

class ServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ServerSocketChannel"
    accept = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    open = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/ServerSocketChannel;", True, False), ("()Ljava/nio/channels/ServerSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;I)Ljava/nio/channels/ServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/ServerSocketChannel;", False, False)])
    socket = JavaMethod("()Ljava/net/ServerSocket;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/ServerSocketChannel;", False, False)])
    validOps = JavaMethod("()I")

class AlreadyConnectedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AlreadyConnectedException"
    __javaconstructor__ = [("()V", False)]

class ScatteringByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ScatteringByteChannel"
    read = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])

class WritePendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/WritePendingException"
    __javaconstructor__ = [("()V", False)]

class IllegalChannelGroupException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalChannelGroupException"
    __javaconstructor__ = [("()V", False)]

class SelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectionKey"
    OP_READ = JavaStaticField("I")
    OP_WRITE = JavaStaticField("I")
    OP_CONNECT = JavaStaticField("I")
    OP_ACCEPT = JavaStaticField("I")
    isConnectable = JavaMethod("()Z")
    isReadable = JavaMethod("()Z")
    isWritable = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    attach = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    channel = JavaMethod("()Ljava/nio/channels/SelectableChannel;")
    isValid = JavaMethod("()Z")
    selector = JavaMethod("()Ljava/nio/channels/Selector;")
    attachment = JavaMethod("()Ljava/lang/Object;")
    readyOps = JavaMethod("()I")
    interestOpsOr = JavaMethod("(I)I")
    interestOpsAnd = JavaMethod("(I)I")
    isAcceptable = JavaMethod("()Z")
    interestOps = JavaMultipleMethod([("()I", False, False), ("(I)Ljava/nio/channels/SelectionKey;", False, False)])

class AsynchronousServerSocketChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousServerSocketChannel"
    provider = JavaMethod("()Ljava/nio/channels/spi/AsynchronousChannelProvider;")
    accept = JavaMultipleMethod([("()Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    open = JavaMultipleMethod([("()Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False), ("(Ljava/nio/channels/AsynchronousChannelGroup;)Ljava/nio/channels/AsynchronousServerSocketChannel;", True, False)])
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketAddress;I)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False), ("(Ljava/net/SocketAddress;)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False)])
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMultipleMethod([("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;", False, False), ("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/AsynchronousServerSocketChannel;", False, False)])

class ShutdownChannelGroupException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ShutdownChannelGroupException"
    __javaconstructor__ = [("()V", False)]

class NonReadableChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NonReadableChannelException"
    __javaconstructor__ = [("()V", False)]

class AsynchronousCloseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousCloseException"
    __javaconstructor__ = [("()V", False)]

class ClosedByInterruptException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedByInterruptException"
    __javaconstructor__ = [("()V", False)]

class SeekableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SeekableByteChannel"
    size = JavaMethod("()J")
    position = JavaMultipleMethod([("(J)Ljava/nio/channels/SeekableByteChannel;", False, False), ("()J", False, False)])
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    truncate = JavaMethod("(J)Ljava/nio/channels/SeekableByteChannel;")

class FileLockInterruptionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileLockInterruptionException"
    __javaconstructor__ = [("()V", False)]

class ReadableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ReadableByteChannel"
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")

class Selector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Selector"
    select = JavaMultipleMethod([("(J)I", False, False), ("(Ljava/util/function/Consumer;J)I", False, False), ("(Ljava/util/function/Consumer;)I", False, False), ("()I", False, False)])
    isOpen = JavaMethod("()Z")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    close = JavaMethod("()V")
    keys = JavaMethod("()Ljava/util/Set;")
    open = JavaStaticMethod("()Ljava/nio/channels/Selector;")
    selectedKeys = JavaMethod("()Ljava/util/Set;")
    selectNow = JavaMultipleMethod([("(Ljava/util/function/Consumer;)I", False, False), ("()I", False, False)])
    wakeup = JavaMethod("()Ljava/nio/channels/Selector;")

class MulticastChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/MulticastChannel"
    join = JavaMultipleMethod([("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;)Ljava/nio/channels/MembershipKey;", False, False), ("(Ljava/net/InetAddress;Ljava/net/NetworkInterface;Ljava/net/InetAddress;)Ljava/nio/channels/MembershipKey;", False, False)])
    close = JavaMethod("()V")

class IllegalBlockingModeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalBlockingModeException"
    __javaconstructor__ = [("()V", False)]

class ClosedSelectorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedSelectorException"
    __javaconstructor__ = [("()V", False)]

class AsynchronousByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousByteChannel"
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])

class ClosedChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedChannelException"
    __javaconstructor__ = [("()V", False)]

class FileLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileLock"
    isShared = JavaMethod("()Z")
    size = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    position = JavaMethod("()J")
    close = JavaMethod("()V")
    channel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    isValid = JavaMethod("()Z")
    release = JavaMethod("()V")
    acquiredBy = JavaMethod("()Ljava/nio/channels/Channel;")
    overlaps = JavaMethod("(JJ)Z")

class AlreadyBoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AlreadyBoundException"
    __javaconstructor__ = [("()V", False)]

class FileChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileChannel"
    force = JavaMethod("(Z)V")
    lock = JavaMultipleMethod([("()Ljava/nio/channels/FileLock;", False, False), ("(JJZ)Ljava/nio/channels/FileLock;", False, False)])
    size = JavaMethod("()J")
    position = JavaMultipleMethod([("(J)Ljava/nio/channels/FileChannel;", False, False), ("()J", False, False), ("(J)Ljava/nio/channels/SeekableByteChannel;", False, False)])
    map = JavaMultipleMethod([("(Ljava/nio/channels/FileChannel$MapMode;JJLjava/lang/foreign/Arena;)Ljava/lang/foreign/MemorySegment;", False, False), ("(Ljava/nio/channels/FileChannel$MapMode;JJ)Ljava/nio/MappedByteBuffer;", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;J)I", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;J)I", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False)])
    open = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/FileChannel;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/FileChannel;", True, True)])
    tryLock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])
    transferTo = JavaMethod("(JJLjava/nio/channels/WritableByteChannel;)J")
    truncate = JavaMultipleMethod([("(J)Ljava/nio/channels/SeekableByteChannel;", False, False), ("(J)Ljava/nio/channels/FileChannel;", False, False)])
    transferFrom = JavaMethod("(Ljava/nio/channels/ReadableByteChannel;JJ)J")

    class MapMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/FileChannel$MapMode"
        READ_ONLY = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        READ_WRITE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        PRIVATE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        toString = JavaMethod("()Ljava/lang/String;")

class AsynchronousFileChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousFileChannel"
    force = JavaMethod("(Z)V")
    lock = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(JJZLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("()Ljava/util/concurrent/Future;", False, False), ("(JJZ)Ljava/util/concurrent/Future;", False, False)])
    size = JavaMethod("()J")
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;J)Ljava/util/concurrent/Future;", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;J)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;JLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    open = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;Ljava/util/concurrent/ExecutorService;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/AsynchronousFileChannel;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/AsynchronousFileChannel;", True, True)])
    tryLock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])
    truncate = JavaMethod("(J)Ljava/nio/channels/AsynchronousFileChannel;")

class Channels(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Channels"
    newInputStream = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousByteChannel;)Ljava/io/InputStream;", True, False), ("(Ljava/nio/channels/ReadableByteChannel;)Ljava/io/InputStream;", True, False)])
    newOutputStream = JavaMultipleMethod([("(Ljava/nio/channels/AsynchronousByteChannel;)Ljava/io/OutputStream;", True, False), ("(Ljava/nio/channels/WritableByteChannel;)Ljava/io/OutputStream;", True, False)])
    newReader = JavaMultipleMethod([("(Ljava/nio/channels/ReadableByteChannel;Ljava/lang/String;)Ljava/io/Reader;", True, False), ("(Ljava/nio/channels/ReadableByteChannel;Ljava/nio/charset/CharsetDecoder;I)Ljava/io/Reader;", True, False), ("(Ljava/nio/channels/ReadableByteChannel;Ljava/nio/charset/Charset;)Ljava/io/Reader;", True, False)])
    newWriter = JavaMultipleMethod([("(Ljava/nio/channels/WritableByteChannel;Ljava/nio/charset/CharsetEncoder;I)Ljava/io/Writer;", True, False), ("(Ljava/nio/channels/WritableByteChannel;Ljava/lang/String;)Ljava/io/Writer;", True, False), ("(Ljava/nio/channels/WritableByteChannel;Ljava/nio/charset/Charset;)Ljava/io/Writer;", True, False)])
    newChannel = JavaMultipleMethod([("(Ljava/io/InputStream;)Ljava/nio/channels/ReadableByteChannel;", True, False), ("(Ljava/io/OutputStream;)Ljava/nio/channels/WritableByteChannel;", True, False)])

class WritableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/WritableByteChannel"
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")

class InterruptibleChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/InterruptibleChannel"
    close = JavaMethod("()V")

class UnsupportedAddressTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/UnsupportedAddressTypeException"
    __javaconstructor__ = [("()V", False)]

class AcceptPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AcceptPendingException"
    __javaconstructor__ = [("()V", False)]

class ReadPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ReadPendingException"
    __javaconstructor__ = [("()V", False)]

class AsynchronousChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousChannel"
    close = JavaMethod("()V")

class ConnectionPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ConnectionPendingException"
    __javaconstructor__ = [("()V", False)]

class NotYetBoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NotYetBoundException"
    __javaconstructor__ = [("()V", False)]
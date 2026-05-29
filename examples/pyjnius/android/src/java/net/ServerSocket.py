from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocket"]

class ServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ServerSocket"
    __javaconstructor__ = [("(II)V", False), ("(IILjava/net/InetAddress;)V", False), ("(I)V", False), ("()V", False)]
    getInetAddress = JavaMethod("()Ljava/net/InetAddress;")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    accept = JavaMethod("()Ljava/net/Socket;")
    isBound = JavaMethod("()Z")
    isClosed = JavaMethod("()Z")
    getChannel = JavaMethod("()Ljava/nio/channels/ServerSocketChannel;")
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)V", False, False), ("(Ljava/net/SocketAddress;I)V", False, False)])
    setSocketFactory = JavaStaticMethod("(Ljava/net/SocketImplFactory;)V")
    getLocalSocketAddress = JavaMethod("()Ljava/net/SocketAddress;")
    getLocalPort = JavaMethod("()I")
    setSoTimeout = JavaMethod("(I)V")
    getSoTimeout = JavaMethod("()I")
    setReceiveBufferSize = JavaMethod("(I)V")
    getReceiveBufferSize = JavaMethod("()I")
    setReuseAddress = JavaMethod("(Z)V")
    getReuseAddress = JavaMethod("()Z")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/net/ServerSocket;")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
    setPerformancePreferences = JavaMethod("(III)V")
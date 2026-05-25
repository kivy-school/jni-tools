from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocket"]

class ServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ServerSocket"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(II)V", False), ("(IILjava/net/InetAddress;)V", False)]
    bind = JavaMultipleMethod([("(Ljava/net/SocketAddress;)V", False, False), ("(Ljava/net/SocketAddress;I)V", False, False)])
    getInetAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalPort = JavaMethod("()I")
    getLocalSocketAddress = JavaMethod("()Ljava/net/SocketAddress;")
    accept = JavaMethod("()Ljava/net/Socket;")
    implAccept = JavaMethod("(Ljava/net/Socket;)V")
    close = JavaMethod("()V")
    getChannel = JavaMethod("()Ljava/nio/channels/ServerSocketChannel;")
    isBound = JavaMethod("()Z")
    isClosed = JavaMethod("()Z")
    setSoTimeout = JavaMethod("(I)V")
    getSoTimeout = JavaMethod("()I")
    setReuseAddress = JavaMethod("(Z)V")
    getReuseAddress = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    setSocketFactory = JavaStaticMethod("(Ljava/net/SocketImplFactory;)V")
    setReceiveBufferSize = JavaMethod("(I)V")
    getReceiveBufferSize = JavaMethod("()I")
    setPerformancePreferences = JavaMethod("(III)V")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/net/ServerSocket;")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
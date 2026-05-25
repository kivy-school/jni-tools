from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketImpl"]

class SocketImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketImpl"
    __javaconstructor__ = [("()V", False)]
    address = JavaField("Ljava/net/InetAddress;")
    fd = JavaField("Ljava/io/FileDescriptor;")
    localport = JavaField("I")
    port = JavaField("I")
    create = JavaMethod("(Z)V")
    connect = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/net/InetAddress;I)V", False, False), ("(Ljava/net/SocketAddress;I)V", False, False)])
    bind = JavaMethod("(Ljava/net/InetAddress;I)V")
    listen = JavaMethod("(I)V")
    accept = JavaMethod("(Ljava/net/SocketImpl;)V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    shutdownInput = JavaMethod("()V")
    shutdownOutput = JavaMethod("()V")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getInetAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    supportsUrgentData = JavaMethod("()Z")
    sendUrgentData = JavaMethod("(I)V")
    getLocalPort = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    setPerformancePreferences = JavaMethod("(III)V")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)V")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
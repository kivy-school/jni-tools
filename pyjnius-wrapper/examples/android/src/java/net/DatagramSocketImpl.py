from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramSocketImpl"]

class DatagramSocketImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/DatagramSocketImpl"
    __javaconstructor__ = [("()V", False)]
    fd = JavaField("Ljava/io/FileDescriptor;")
    localPort = JavaField("I")
    create = JavaMethod("()V")
    bind = JavaMethod("(ILjava/net/InetAddress;)V")
    send = JavaMethod("(Ljava/net/DatagramPacket;)V")
    connect = JavaMethod("(Ljava/net/InetAddress;I)V")
    disconnect = JavaMethod("()V")
    peek = JavaMethod("(Ljava/net/InetAddress;)I")
    peekData = JavaMethod("(Ljava/net/DatagramPacket;)I")
    receive = JavaMethod("(Ljava/net/DatagramPacket;)V")
    setTTL = JavaMethod("(B)V")
    getTTL = JavaMethod("()B")
    setTimeToLive = JavaMethod("(I)V")
    getTimeToLive = JavaMethod("()I")
    join = JavaMethod("(Ljava/net/InetAddress;)V")
    leave = JavaMethod("(Ljava/net/InetAddress;)V")
    joinGroup = JavaMethod("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V")
    leaveGroup = JavaMethod("(Ljava/net/SocketAddress;Ljava/net/NetworkInterface;)V")
    close = JavaMethod("()V")
    getLocalPort = JavaMethod("()I")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)V")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
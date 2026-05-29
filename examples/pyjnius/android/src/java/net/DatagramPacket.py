from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramPacket"]

class DatagramPacket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/DatagramPacket"
    __javaconstructor__ = [("([BILjava/net/InetAddress;I)V", False), ("([BILjava/net/SocketAddress;)V", False), ("([BII)V", False), ("([BI)V", False), ("([BIILjava/net/InetAddress;I)V", False), ("([BIILjava/net/SocketAddress;)V", False)]
    setPort = JavaMethod("(I)V")
    setAddress = JavaMethod("(Ljava/net/InetAddress;)V")
    getLength = JavaMethod("()I")
    setLength = JavaMethod("(I)V")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    setSocketAddress = JavaMethod("(Ljava/net/SocketAddress;)V")
    getSocketAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setData = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    getOffset = JavaMethod("()I")
    getData = JavaMethod("()[B")
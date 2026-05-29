from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramPacket"]

class DatagramPacket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/DatagramPacket"
    __javaconstructor__ = [("([BII)V", False), ("([BI)V", False), ("([BIILjava/net/InetAddress;I)V", False), ("([BIILjava/net/SocketAddress;)V", False), ("([BILjava/net/InetAddress;I)V", False), ("([BILjava/net/SocketAddress;)V", False)]
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    getData = JavaMethod("()[B")
    getOffset = JavaMethod("()I")
    getLength = JavaMethod("()I")
    setData = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False)])
    setAddress = JavaMethod("(Ljava/net/InetAddress;)V")
    setPort = JavaMethod("(I)V")
    setSocketAddress = JavaMethod("(Ljava/net/SocketAddress;)V")
    getSocketAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setLength = JavaMethod("(I)V")
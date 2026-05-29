from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardSocketOptions"]

class StandardSocketOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/StandardSocketOptions"
    SO_BROADCAST = JavaStaticField("Ljava/net/SocketOption;")
    SO_KEEPALIVE = JavaStaticField("Ljava/net/SocketOption;")
    SO_SNDBUF = JavaStaticField("Ljava/net/SocketOption;")
    SO_RCVBUF = JavaStaticField("Ljava/net/SocketOption;")
    SO_REUSEADDR = JavaStaticField("Ljava/net/SocketOption;")
    SO_REUSEPORT = JavaStaticField("Ljava/net/SocketOption;")
    SO_LINGER = JavaStaticField("Ljava/net/SocketOption;")
    IP_TOS = JavaStaticField("Ljava/net/SocketOption;")
    IP_MULTICAST_IF = JavaStaticField("Ljava/net/SocketOption;")
    IP_MULTICAST_TTL = JavaStaticField("Ljava/net/SocketOption;")
    IP_MULTICAST_LOOP = JavaStaticField("Ljava/net/SocketOption;")
    TCP_NODELAY = JavaStaticField("Ljava/net/SocketOption;")
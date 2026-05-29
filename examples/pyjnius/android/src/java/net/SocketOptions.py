from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketOptions"]

class SocketOptions(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketOptions"
    IP_MULTICAST_IF = JavaStaticField("I")
    IP_MULTICAST_IF2 = JavaStaticField("I")
    IP_MULTICAST_LOOP = JavaStaticField("I")
    IP_TOS = JavaStaticField("I")
    SO_BINDADDR = JavaStaticField("I")
    SO_BROADCAST = JavaStaticField("I")
    SO_KEEPALIVE = JavaStaticField("I")
    SO_LINGER = JavaStaticField("I")
    SO_OOBINLINE = JavaStaticField("I")
    SO_RCVBUF = JavaStaticField("I")
    SO_REUSEADDR = JavaStaticField("I")
    SO_REUSEPORT = JavaStaticField("I")
    SO_SNDBUF = JavaStaticField("I")
    SO_TIMEOUT = JavaStaticField("I")
    TCP_NODELAY = JavaStaticField("I")
    setOption = JavaMethod("(ILjava/lang/Object;)V")
    getOption = JavaMethod("(I)Ljava/lang/Object;")
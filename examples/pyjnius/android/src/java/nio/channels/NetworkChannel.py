from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkChannel"]

class NetworkChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NetworkChannel"
    bind = JavaMethod("(Ljava/net/SocketAddress;)Ljava/nio/channels/NetworkChannel;")
    getLocalAddress = JavaMethod("()Ljava/net/SocketAddress;")
    setOption = JavaMethod("(Ljava/net/SocketOption;Ljava/lang/Object;)Ljava/nio/channels/NetworkChannel;")
    getOption = JavaMethod("(Ljava/net/SocketOption;)Ljava/lang/Object;")
    supportedOptions = JavaMethod("()Ljava/util/Set;")
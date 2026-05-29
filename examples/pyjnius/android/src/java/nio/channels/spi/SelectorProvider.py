from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectorProvider"]

class SelectorProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/SelectorProvider"
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    inheritedChannel = JavaMethod("()Ljava/nio/channels/Channel;")
    openDatagramChannel = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", False, False), ("()Ljava/nio/channels/DatagramChannel;", False, False)])
    openSocketChannel = JavaMultipleMethod([("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/SocketChannel;", False, False), ("()Ljava/nio/channels/SocketChannel;", False, False)])
    openServerSocketChannel = JavaMultipleMethod([("()Ljava/nio/channels/ServerSocketChannel;", False, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/ServerSocketChannel;", False, False)])
    openSelector = JavaMethod("()Ljava/nio/channels/spi/AbstractSelector;")
    openPipe = JavaMethod("()Ljava/nio/channels/Pipe;")
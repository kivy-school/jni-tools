from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectorProvider"]

class SelectorProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/SelectorProvider"
    __javaconstructor__ = [("()V", False)]
    provider = JavaStaticMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    openDatagramChannel = JavaMultipleMethod([("()Ljava/nio/channels/DatagramChannel;", False, False), ("(Ljava/net/ProtocolFamily;)Ljava/nio/channels/DatagramChannel;", False, False)])
    openPipe = JavaMethod("()Ljava/nio/channels/Pipe;")
    openSelector = JavaMethod("()Ljava/nio/channels/spi/AbstractSelector;")
    openServerSocketChannel = JavaMethod("()Ljava/nio/channels/ServerSocketChannel;")
    openSocketChannel = JavaMethod("()Ljava/nio/channels/SocketChannel;")
    inheritedChannel = JavaMethod("()Ljava/nio/channels/Channel;")
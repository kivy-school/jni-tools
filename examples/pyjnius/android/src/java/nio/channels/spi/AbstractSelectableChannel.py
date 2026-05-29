from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelectableChannel"]

class AbstractSelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectableChannel"
    isBlocking = JavaMethod("()Z")
    isRegistered = JavaMethod("()Z")
    register = JavaMethod("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
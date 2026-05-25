from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelectableChannel"]

class AbstractSelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectableChannel"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    isRegistered = JavaMethod("()Z")
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    register = JavaMethod("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;")
    implCloseChannel = JavaMethod("()V")
    implCloseSelectableChannel = JavaMethod("()V")
    isBlocking = JavaMethod("()Z")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")
    implConfigureBlocking = JavaMethod("(Z)V")
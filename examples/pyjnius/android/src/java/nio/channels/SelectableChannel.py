from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectableChannel"]

class SelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectableChannel"
    isBlocking = JavaMethod("()Z")
    isRegistered = JavaMethod("()Z")
    register = JavaMultipleMethod([("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;", False, False), ("(Ljava/nio/channels/Selector;I)Ljava/nio/channels/SelectionKey;", False, False)])
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")
    validOps = JavaMethod("()I")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
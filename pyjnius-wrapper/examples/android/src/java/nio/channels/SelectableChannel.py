from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectableChannel"]

class SelectableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectableChannel"
    __javaconstructor__ = [("()V", False)]
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    validOps = JavaMethod("()I")
    isRegistered = JavaMethod("()Z")
    keyFor = JavaMethod("(Ljava/nio/channels/Selector;)Ljava/nio/channels/SelectionKey;")
    register = JavaMultipleMethod([("(Ljava/nio/channels/Selector;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;", False, False), ("(Ljava/nio/channels/Selector;I)Ljava/nio/channels/SelectionKey;", False, False)])
    configureBlocking = JavaMethod("(Z)Ljava/nio/channels/SelectableChannel;")
    isBlocking = JavaMethod("()Z")
    blockingLock = JavaMethod("()Ljava/lang/Object;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelector"]

class AbstractSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelector"
    __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
    close = JavaMethod("()V")
    implCloseSelector = JavaMethod("()V")
    isOpen = JavaMethod("()Z")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    cancelledKeys = JavaMethod("()Ljava/util/Set;")
    register = JavaMethod("(Ljava/nio/channels/spi/AbstractSelectableChannel;ILjava/lang/Object;)Ljava/nio/channels/SelectionKey;")
    deregister = JavaMethod("(Ljava/nio/channels/spi/AbstractSelectionKey;)V")
    begin = JavaMethod("()V")
    end = JavaMethod("()V")
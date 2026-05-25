from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Selector"]

class Selector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Selector"
    __javaconstructor__ = [("()V", False)]
    open = JavaStaticMethod("()Ljava/nio/channels/Selector;")
    isOpen = JavaMethod("()Z")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    keys = JavaMethod("()Ljava/util/Set;")
    selectedKeys = JavaMethod("()Ljava/util/Set;")
    selectNow = JavaMultipleMethod([("()I", False, False), ("(Ljava/util/function/Consumer;)I", False, False)])
    select = JavaMultipleMethod([("(J)I", False, False), ("()I", False, False), ("(Ljava/util/function/Consumer;J)I", False, False), ("(Ljava/util/function/Consumer;)I", False, False)])
    wakeup = JavaMethod("()Ljava/nio/channels/Selector;")
    close = JavaMethod("()V")
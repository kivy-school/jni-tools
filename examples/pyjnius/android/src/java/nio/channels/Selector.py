from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Selector"]

class Selector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Selector"
    select = JavaMultipleMethod([("(J)I", False, False), ("(Ljava/util/function/Consumer;J)I", False, False), ("(Ljava/util/function/Consumer;)I", False, False), ("()I", False, False)])
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
    keys = JavaMethod("()Ljava/util/Set;")
    open = JavaStaticMethod("()Ljava/nio/channels/Selector;")
    selectedKeys = JavaMethod("()Ljava/util/Set;")
    selectNow = JavaMultipleMethod([("(Ljava/util/function/Consumer;)I", False, False), ("()I", False, False)])
    wakeup = JavaMethod("()Ljava/nio/channels/Selector;")
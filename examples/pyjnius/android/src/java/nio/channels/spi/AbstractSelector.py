from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelector"]

class AbstractSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelector"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    provider = JavaMethod("()Ljava/nio/channels/spi/SelectorProvider;")
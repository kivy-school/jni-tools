from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractInterruptibleChannel"]

class AbstractInterruptibleChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractInterruptibleChannel"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
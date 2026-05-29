from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractInterruptibleChannel"]

class AbstractInterruptibleChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractInterruptibleChannel"
    __javaconstructor__ = [("()V", False)]
    close = JavaMethod("()V")
    implCloseChannel = JavaMethod("()V")
    isOpen = JavaMethod("()Z")
    begin = JavaMethod("()V")
    end = JavaMethod("(Z)V")
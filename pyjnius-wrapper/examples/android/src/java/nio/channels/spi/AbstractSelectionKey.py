from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelectionKey"]

class AbstractSelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectionKey"
    __javaconstructor__ = [("()V", False)]
    isValid = JavaMethod("()Z")
    cancel = JavaMethod("()V")
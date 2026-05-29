from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedSelectorException"]

class ClosedSelectorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedSelectorException"
    __javaconstructor__ = [("()V", False)]
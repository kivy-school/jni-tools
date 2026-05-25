from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalSelectorException"]

class IllegalSelectorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalSelectorException"
    __javaconstructor__ = [("()V", False)]
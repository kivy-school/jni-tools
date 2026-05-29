from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedByInterruptException"]

class ClosedByInterruptException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedByInterruptException"
    __javaconstructor__ = [("()V", False)]
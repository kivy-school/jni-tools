from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotYetBoundException"]

class NotYetBoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NotYetBoundException"
    __javaconstructor__ = [("()V", False)]
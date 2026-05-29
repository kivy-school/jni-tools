from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedChannelException"]

class ClosedChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ClosedChannelException"
    __javaconstructor__ = [("()V", False)]
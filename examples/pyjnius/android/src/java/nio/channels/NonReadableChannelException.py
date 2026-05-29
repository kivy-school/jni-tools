from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NonReadableChannelException"]

class NonReadableChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NonReadableChannelException"
    __javaconstructor__ = [("()V", False)]
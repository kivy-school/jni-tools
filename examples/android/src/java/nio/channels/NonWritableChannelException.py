from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NonWritableChannelException"]

class NonWritableChannelException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NonWritableChannelException"
    __javaconstructor__ = [("()V", False)]
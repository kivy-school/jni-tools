from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadPendingException"]

class ReadPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ReadPendingException"
    __javaconstructor__ = [("()V", False)]
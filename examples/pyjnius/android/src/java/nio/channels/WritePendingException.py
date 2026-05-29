from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WritePendingException"]

class WritePendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/WritePendingException"
    __javaconstructor__ = [("()V", False)]
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionPendingException"]

class ConnectionPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ConnectionPendingException"
    __javaconstructor__ = [("()V", False)]
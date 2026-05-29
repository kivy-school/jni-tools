from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoConnectionPendingException"]

class NoConnectionPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NoConnectionPendingException"
    __javaconstructor__ = [("()V", False)]
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotYetConnectedException"]

class NotYetConnectedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/NotYetConnectedException"
    __javaconstructor__ = [("()V", False)]
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketAddress"]

class SocketAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketAddress"
    __javaconstructor__ = [("()V", False)]
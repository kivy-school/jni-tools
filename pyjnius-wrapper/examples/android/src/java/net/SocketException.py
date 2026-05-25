from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketException"]

class SocketException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketTimeoutException"]

class SocketTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketTimeoutException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
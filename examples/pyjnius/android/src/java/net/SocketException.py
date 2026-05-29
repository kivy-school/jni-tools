from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketException"]

class SocketException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("()V", False), ("(Ljava/lang/String;)V", False)]
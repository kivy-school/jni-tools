from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectException"]

class ConnectException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ConnectException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
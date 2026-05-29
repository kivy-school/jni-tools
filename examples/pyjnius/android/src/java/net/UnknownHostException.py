from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownHostException"]

class UnknownHostException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/UnknownHostException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
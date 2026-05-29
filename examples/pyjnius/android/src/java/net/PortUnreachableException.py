from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PortUnreachableException"]

class PortUnreachableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/PortUnreachableException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
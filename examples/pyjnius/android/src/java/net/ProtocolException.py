from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProtocolException"]

class ProtocolException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ProtocolException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
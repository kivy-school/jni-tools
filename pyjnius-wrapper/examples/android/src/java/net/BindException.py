from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BindException"]

class BindException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/BindException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
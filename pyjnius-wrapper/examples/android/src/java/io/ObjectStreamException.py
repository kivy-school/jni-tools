from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamException"]

class ObjectStreamException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
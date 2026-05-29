from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotSerializableException"]

class NotSerializableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/NotSerializableException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
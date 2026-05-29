from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamCorruptedException"]

class StreamCorruptedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StreamCorruptedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]
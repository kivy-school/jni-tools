from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequenceInputStream"]

class SequenceInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/SequenceInputStream"
    __javaconstructor__ = [("(Ljava/util/Enumeration;)V", False), ("(Ljava/io/InputStream;Ljava/io/InputStream;)V", False)]
    available = JavaMethod("()I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    close = JavaMethod("()V")
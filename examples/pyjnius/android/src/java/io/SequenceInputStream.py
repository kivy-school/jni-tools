from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequenceInputStream"]

class SequenceInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/SequenceInputStream"
    __javaconstructor__ = [("(Ljava/util/Enumeration;)V", False), ("(Ljava/io/InputStream;Ljava/io/InputStream;)V", False)]
    close = JavaMethod("()V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    available = JavaMethod("()I")
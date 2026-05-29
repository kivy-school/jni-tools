from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedInputStream"]

class PipedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedInputStream"
    __javaconstructor__ = [("(Ljava/io/PipedOutputStream;)V", False), ("(I)V", False), ("()V", False), ("(Ljava/io/PipedOutputStream;I)V", False)]
    connect = JavaMethod("(Ljava/io/PipedOutputStream;)V")
    close = JavaMethod("()V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    available = JavaMethod("()I")
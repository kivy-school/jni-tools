from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedOutputStream"]

class PipedOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedOutputStream"
    __javaconstructor__ = [("(Ljava/io/PipedInputStream;)V", False), ("()V", False)]
    connect = JavaMethod("(Ljava/io/PipedInputStream;)V")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False)])
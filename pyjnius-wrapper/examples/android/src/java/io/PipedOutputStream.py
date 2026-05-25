from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedOutputStream"]

class PipedOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedOutputStream"
    __javaconstructor__ = [("(Ljava/io/PipedInputStream;)V", False), ("()V", False)]
    connect = JavaMethod("(Ljava/io/PipedInputStream;)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
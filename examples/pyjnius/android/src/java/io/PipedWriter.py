from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedWriter"]

class PipedWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedWriter"
    __javaconstructor__ = [("(Ljava/io/PipedReader;)V", False), ("()V", False)]
    connect = JavaMethod("(Ljava/io/PipedReader;)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
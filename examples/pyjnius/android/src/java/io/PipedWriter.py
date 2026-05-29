from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedWriter"]

class PipedWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedWriter"
    __javaconstructor__ = [("(Ljava/io/PipedReader;)V", False), ("()V", False)]
    connect = JavaMethod("(Ljava/io/PipedReader;)V")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([CII)V", False, False), ("(I)V", False, False)])
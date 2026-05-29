from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedReader"]

class PipedReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedReader"
    __javaconstructor__ = [("(Ljava/io/PipedWriter;)V", False), ("(I)V", False), ("()V", False), ("(Ljava/io/PipedWriter;I)V", False)]
    connect = JavaMethod("(Ljava/io/PipedWriter;)V")
    close = JavaMethod("()V")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    ready = JavaMethod("()Z")
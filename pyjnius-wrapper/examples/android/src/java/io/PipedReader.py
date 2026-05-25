from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedReader"]

class PipedReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedReader"
    __javaconstructor__ = [("(Ljava/io/PipedWriter;)V", False), ("(Ljava/io/PipedWriter;I)V", False), ("()V", False), ("(I)V", False)]
    connect = JavaMethod("(Ljava/io/PipedWriter;)V")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    ready = JavaMethod("()Z")
    close = JavaMethod("()V")
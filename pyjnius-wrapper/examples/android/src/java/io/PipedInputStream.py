from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PipedInputStream"]

class PipedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PipedInputStream"
    __javaconstructor__ = [("(Ljava/io/PipedOutputStream;)V", False), ("(Ljava/io/PipedOutputStream;I)V", False), ("()V", False), ("(I)V", False)]
    PIPE_SIZE = JavaStaticField("I")
    buffer = JavaField("[B")
    in = JavaField("I")
    out = JavaField("I")
    connect = JavaMethod("(Ljava/io/PipedOutputStream;)V")
    receive = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    available = JavaMethod("()I")
    close = JavaMethod("()V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedOutputStream"]

class BufferedOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;I)V", False)]
    buf = JavaField("[B")
    count = JavaField("I")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
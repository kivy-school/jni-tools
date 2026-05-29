from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeflaterOutputStream"]

class DeflaterOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/DeflaterOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/util/zip/Deflater;IZ)V", False), ("(Ljava/io/OutputStream;Ljava/util/zip/Deflater;I)V", False), ("(Ljava/io/OutputStream;Ljava/util/zip/Deflater;Z)V", False), ("(Ljava/io/OutputStream;Ljava/util/zip/Deflater;)V", False), ("(Ljava/io/OutputStream;Z)V", False), ("(Ljava/io/OutputStream;)V", False)]
    buf = JavaField("[B")
    def = JavaField("Ljava/util/zip/Deflater;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    finish = JavaMethod("()V")
    close = JavaMethod("()V")
    deflate = JavaMethod("()V")
    flush = JavaMethod("()V")
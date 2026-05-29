from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeflaterInputStream"]

class DeflaterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/DeflaterInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;Ljava/util/zip/Deflater;)V", False), ("(Ljava/io/InputStream;Ljava/util/zip/Deflater;I)V", False)]
    buf = JavaField("[B")
    def = JavaField("Ljava/util/zip/Deflater;")
    close = JavaMethod("()V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
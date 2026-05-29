from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeflaterInputStream"]

class DeflaterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/DeflaterInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/util/zip/Deflater;)V", False), ("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;Ljava/util/zip/Deflater;I)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
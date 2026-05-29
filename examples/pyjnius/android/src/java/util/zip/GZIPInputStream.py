from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GZIPInputStream"]

class GZIPInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/GZIPInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;I)V", False)]
    GZIP_MAGIC = JavaStaticField("I")
    close = JavaMethod("()V")
    read = JavaMethod("([BII)I")
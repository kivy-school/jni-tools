from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GZIPInputStream"]

class GZIPInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/GZIPInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;I)V", False), ("(Ljava/io/InputStream;)V", False)]
    GZIP_MAGIC = JavaStaticField("I")
    crc = JavaField("Ljava/util/zip/CRC32;")
    eos = JavaField("Z")
    read = JavaMethod("([BII)I")
    close = JavaMethod("()V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CheckedInputStream"]

class CheckedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/CheckedInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/util/zip/Checksum;)V", False)]
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    getChecksum = JavaMethod("()Ljava/util/zip/Checksum;")
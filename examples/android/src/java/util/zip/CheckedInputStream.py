from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CheckedInputStream"]

class CheckedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/CheckedInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/util/zip/Checksum;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    getChecksum = JavaMethod("()Ljava/util/zip/Checksum;")
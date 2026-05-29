from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CheckedOutputStream"]

class CheckedOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/CheckedOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/util/zip/Checksum;)V", False)]
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False)])
    getChecksum = JavaMethod("()Ljava/util/zip/Checksum;")
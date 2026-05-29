from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GZIPOutputStream"]

class GZIPOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/GZIPOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Z)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;IZ)V", False), ("(Ljava/io/OutputStream;I)V", False)]
    write = JavaMethod("([BII)V")
    finish = JavaMethod("()V")
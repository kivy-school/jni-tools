from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InflaterOutputStream"]

class InflaterOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/InflaterOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/util/zip/Inflater;)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Ljava/util/zip/Inflater;I)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    finish = JavaMethod("()V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InflaterInputStream"]

class InflaterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/InflaterInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/util/zip/Inflater;I)V", False), ("(Ljava/io/InputStream;Ljava/util/zip/Inflater;)V", False), ("(Ljava/io/InputStream;)V", False)]
    buf = JavaField("[B")
    closed = JavaField("Z")
    inf = JavaField("Ljava/util/zip/Inflater;")
    len = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    available = JavaMethod("()I")
    skip = JavaMethod("(J)J")
    close = JavaMethod("()V")
    fill = JavaMethod("()V")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
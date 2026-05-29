from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InflaterInputStream"]

class InflaterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/InflaterInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/util/zip/Inflater;)V", False), ("(Ljava/io/InputStream;Ljava/util/zip/Inflater;I)V", False), ("(Ljava/io/InputStream;)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
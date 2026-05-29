from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedInputStream"]

class BufferedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;I)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
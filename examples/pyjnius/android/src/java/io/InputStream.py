from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputStream"]

class InputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InputStream"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    readAllBytes = JavaMethod("()[B")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([B)I", False, False), ("([BII)I", False, False), ("()I", False, False)])
    readNBytes = JavaMultipleMethod([("([BII)I", False, False), ("(I)[B", False, False)])
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
    nullInputStream = JavaStaticMethod("()Ljava/io/InputStream;")
    skipNBytes = JavaMethod("(J)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputStream"]

class InputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InputStream"
    __javaconstructor__ = [("()V", False)]
    nullInputStream = JavaStaticMethod("()Ljava/io/InputStream;")
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    readAllBytes = JavaMethod("()[B")
    readNBytes = JavaMultipleMethod([("(I)[B", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    skipNBytes = JavaMethod("(J)V")
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    markSupported = JavaMethod("()Z")
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
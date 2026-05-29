from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteArrayInputStream"]

class ByteArrayInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ByteArrayInputStream"
    __javaconstructor__ = [("([B)V", False), ("([BII)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    readAllBytes = JavaMethod("()[B")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    readNBytes = JavaMethod("([BII)I")
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
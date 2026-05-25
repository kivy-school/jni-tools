from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteArrayInputStream"]

class ByteArrayInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ByteArrayInputStream"
    __javaconstructor__ = [("([B)V", False), ("([BII)V", False)]
    buf = JavaField("[B")
    count = JavaField("I")
    mark = JavaField("I")
    pos = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    readAllBytes = JavaMethod("()[B")
    readNBytes = JavaMethod("([BII)I")
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
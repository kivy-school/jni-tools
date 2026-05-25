from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteArrayOutputStream"]

class ByteArrayOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ByteArrayOutputStream"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    buf = JavaField("[B")
    count = JavaField("I")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    writeBytes = JavaMethod("([B)V")
    writeTo = JavaMethod("(Ljava/io/OutputStream;)V")
    reset = JavaMethod("()V")
    toByteArray = JavaMethod("()[B")
    size = JavaMethod("()I")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/nio/charset/Charset;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    close = JavaMethod("()V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteArrayOutputStream"]

class ByteArrayOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ByteArrayOutputStream"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    size = JavaMethod("()I")
    reset = JavaMethod("()V")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/nio/charset/Charset;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False)])
    writeTo = JavaMethod("(Ljava/io/OutputStream;)V")
    writeBytes = JavaMethod("([B)V")
    toByteArray = JavaMethod("()[B")
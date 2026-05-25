from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutputStreamWriter"]

class OutputStreamWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/OutputStreamWriter"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/lang/String;)V", False), ("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/OutputStream;Ljava/nio/charset/CharsetEncoder;)V", False)]
    getEncoding = JavaMethod("()Ljava/lang/String;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
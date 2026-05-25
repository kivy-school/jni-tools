from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayWriter"]

class CharArrayWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/CharArrayWriter"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    buf = JavaField("[C")
    count = JavaField("I")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    writeTo = JavaMethod("(Ljava/io/Writer;)V")
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/io/CharArrayWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/CharArrayWriter;", False, False), ("(C)Ljava/io/CharArrayWriter;", False, False)])
    reset = JavaMethod("()V")
    toCharArray = JavaMethod("()[C")
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
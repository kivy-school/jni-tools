from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayWriter"]

class CharArrayWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/CharArrayWriter"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    size = JavaMethod("()I")
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(C)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/CharArrayWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/CharArrayWriter;", False, False), ("(C)Ljava/io/CharArrayWriter;", False, False)])
    flush = JavaMethod("()V")
    toCharArray = JavaMethod("()[C")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    writeTo = JavaMethod("(Ljava/io/Writer;)V")
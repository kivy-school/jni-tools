from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Writer"]

class Writer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Writer"
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(C)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("(Ljava/lang/String;II)V", False, False), ("(I)V", False, False), ("(Ljava/lang/String;)V", False, False), ("([CII)V", False, False), ("([C)V", False, False)])
    nullWriter = JavaStaticMethod("()Ljava/io/Writer;")
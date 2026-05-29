from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringWriter"]

class StringWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringWriter"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    getBuffer = JavaMethod("()Ljava/lang/StringBuffer;")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMultipleMethod([("(C)Ljava/io/StringWriter;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(C)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Ljava/io/StringWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/StringWriter;", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("(Ljava/lang/String;II)V", False, False), ("(Ljava/lang/String;)V", False, False), ("([CII)V", False, False), ("(I)V", False, False)])
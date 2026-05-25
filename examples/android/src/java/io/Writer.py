from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Writer"]

class Writer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Writer"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Object;)V", False)]
    lock = JavaField("Ljava/lang/Object;")
    nullWriter = JavaStaticMethod("()Ljava/io/Writer;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([C)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/io/Writer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/Writer;", False, False), ("(C)Ljava/io/Writer;", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
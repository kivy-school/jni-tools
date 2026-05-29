from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringWriter"]

class StringWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StringWriter"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/io/StringWriter;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/io/StringWriter;", False, False), ("(C)Ljava/io/StringWriter;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    getBuffer = JavaMethod("()Ljava/lang/StringBuffer;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
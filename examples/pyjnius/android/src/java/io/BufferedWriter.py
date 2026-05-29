from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedWriter"]

class BufferedWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedWriter"
    __javaconstructor__ = [("(Ljava/io/Writer;)V", False), ("(Ljava/io/Writer;I)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([CII)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(I)V", False, False)])
    newLine = JavaMethod("()V")
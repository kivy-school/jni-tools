from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterWriter"]

class FilterWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterWriter"
    __javaconstructor__ = [("(Ljava/io/Writer;)V", False)]
    out = JavaField("Ljava/io/Writer;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
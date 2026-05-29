from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reader"]

class Reader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Reader"
    reset = JavaMethod("()V")
    of = JavaStaticMethod("(Ljava/lang/CharSequence;)Ljava/io/Reader;")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([CII)I", False, False), ("([C)I", False, False), ("()I", False, False), ("(Ljava/nio/CharBuffer;)I", False, False)])
    transferTo = JavaMethod("(Ljava/io/Writer;)J")
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    nullReader = JavaStaticMethod("()Ljava/io/Reader;")
    readAllAsString = JavaMethod("()Ljava/lang/String;")
    ready = JavaMethod("()Z")
    readAllLines = JavaMethod("()Ljava/util/List;")
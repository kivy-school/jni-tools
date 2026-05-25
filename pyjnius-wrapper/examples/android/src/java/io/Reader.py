from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reader"]

class Reader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Reader"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Object;)V", False)]
    lock = JavaField("Ljava/lang/Object;")
    nullReader = JavaStaticMethod("()Ljava/io/Reader;")
    read = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)I", False, False), ("()I", False, False), ("([C)I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    ready = JavaMethod("()Z")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    transferTo = JavaMethod("(Ljava/io/Writer;)J")
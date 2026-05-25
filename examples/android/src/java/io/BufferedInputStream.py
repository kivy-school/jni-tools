from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedInputStream"]

class BufferedInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;I)V", False)]
    count = JavaField("I")
    marklimit = JavaField("I")
    markpos = JavaField("I")
    pos = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    markSupported = JavaMethod("()Z")
    close = JavaMethod("()V")
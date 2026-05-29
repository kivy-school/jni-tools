from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayReader"]

class CharArrayReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/CharArrayReader"
    __javaconstructor__ = [("([C)V", False), ("([CII)V", False)]
    buf = JavaField("[C")
    count = JavaField("I")
    markedPos = JavaField("I")
    pos = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False), ("(Ljava/nio/CharBuffer;)I", False, False)])
    skip = JavaMethod("(J)J")
    ready = JavaMethod("()Z")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
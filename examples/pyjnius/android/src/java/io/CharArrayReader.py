from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayReader"]

class CharArrayReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/CharArrayReader"
    __javaconstructor__ = [("([C)V", False), ("([CII)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("(Ljava/nio/CharBuffer;)I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    ready = JavaMethod("()Z")
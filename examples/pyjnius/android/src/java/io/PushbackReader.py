from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushbackReader"]

class PushbackReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PushbackReader"
    __javaconstructor__ = [("(Ljava/io/Reader;I)V", False), ("(Ljava/io/Reader;)V", False)]
    unread = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("([C)V", False, False)])
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([CII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    ready = JavaMethod("()Z")
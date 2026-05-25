from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushbackReader"]

class PushbackReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PushbackReader"
    __javaconstructor__ = [("(Ljava/io/Reader;I)V", False), ("(Ljava/io/Reader;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    unread = JavaMultipleMethod([("(I)V", False, False), ("([CII)V", False, False), ("([C)V", False, False)])
    ready = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    markSupported = JavaMethod("()Z")
    close = JavaMethod("()V")
    skip = JavaMethod("(J)J")
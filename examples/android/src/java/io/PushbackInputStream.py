from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushbackInputStream"]

class PushbackInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PushbackInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;I)V", False), ("(Ljava/io/InputStream;)V", False)]
    buf = JavaField("[B")
    pos = JavaField("I")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    unread = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])
    available = JavaMethod("()I")
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
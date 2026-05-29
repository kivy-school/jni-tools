from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PushbackInputStream"]

class PushbackInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/PushbackInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/InputStream;I)V", False)]
    unread = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False), ("([B)V", False, False)])
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    transferTo = JavaMethod("(Ljava/io/OutputStream;)J")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64InputStream"]

class Base64InputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64InputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;I)V", False)]
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64InputStream"]

class Base64InputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64InputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;I)V", False)]
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    available = JavaMethod("()I")
    skip = JavaMethod("(J)J")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
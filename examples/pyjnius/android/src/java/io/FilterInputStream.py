from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterInputStream"]

class FilterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    markSupported = JavaMethod("()Z")
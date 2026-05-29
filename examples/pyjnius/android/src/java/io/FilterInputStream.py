from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterInputStream"]

class FilterInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterInputStream"
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")
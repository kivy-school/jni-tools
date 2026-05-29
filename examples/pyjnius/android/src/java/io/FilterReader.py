from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterReader"]

class FilterReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterReader"
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
    mark = JavaMethod("(I)V")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    markSupported = JavaMethod("()Z")
    ready = JavaMethod("()Z")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterReader"]

class FilterReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterReader"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False)]
    in = JavaField("Ljava/io/Reader;")
    read = JavaMultipleMethod([("()I", False, False), ("([CII)I", False, False)])
    skip = JavaMethod("(J)J")
    ready = JavaMethod("()Z")
    markSupported = JavaMethod("()Z")
    mark = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    close = JavaMethod("()V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterOutputStream"]

class FilterOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False)]
    out = JavaField("Ljava/io/OutputStream;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
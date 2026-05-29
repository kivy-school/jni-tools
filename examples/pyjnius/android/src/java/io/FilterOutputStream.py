from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterOutputStream"]

class FilterOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilterOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([B)V", False, False), ("(I)V", False, False), ("([BII)V", False, False)])
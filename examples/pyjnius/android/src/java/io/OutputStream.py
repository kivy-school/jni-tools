from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutputStream"]

class OutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/OutputStream"
    __javaconstructor__ = [("()V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False), ("(I)V", False, False)])
    nullOutputStream = JavaStaticMethod("()Ljava/io/OutputStream;")
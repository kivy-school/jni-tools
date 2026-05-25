from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutputStream"]

class OutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/OutputStream"
    __javaconstructor__ = [("()V", False)]
    nullOutputStream = JavaStaticMethod("()Ljava/io/OutputStream;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
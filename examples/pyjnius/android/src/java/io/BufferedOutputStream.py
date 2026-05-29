from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferedOutputStream"]

class BufferedOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/BufferedOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False), ("(Ljava/io/OutputStream;I)V", False)]
    flush = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False)])
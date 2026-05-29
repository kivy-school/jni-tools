from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Adler32"]

class Adler32(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Adler32"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    update = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([BII)V", False, False)])
    getValue = JavaMethod("()J")
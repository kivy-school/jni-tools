from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRC32C"]

class CRC32C(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/CRC32C"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    update = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getValue = JavaMethod("()J")
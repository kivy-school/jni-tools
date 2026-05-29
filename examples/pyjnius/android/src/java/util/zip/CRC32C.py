from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRC32C"]

class CRC32C(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/CRC32C"
    __javaconstructor__ = [("()V", False)]
    update = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    reset = JavaMethod("()V")
    getValue = JavaMethod("()J")
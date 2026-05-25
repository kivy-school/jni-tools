from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Checksum"]

class Checksum(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Checksum"
    update = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getValue = JavaMethod("()J")
    reset = JavaMethod("()V")
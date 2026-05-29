from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Checksum"]

class Checksum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Checksum"
    reset = JavaMethod("()V")
    update = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])
    getValue = JavaMethod("()J")
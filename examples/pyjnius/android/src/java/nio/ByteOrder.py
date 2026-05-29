from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteOrder"]

class ByteOrder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/ByteOrder"
    BIG_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
    LITTLE_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
    nativeOrder = JavaStaticMethod("()Ljava/nio/ByteOrder;")
    toString = JavaMethod("()Ljava/lang/String;")
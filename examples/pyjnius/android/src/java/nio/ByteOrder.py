from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteOrder"]

class ByteOrder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/ByteOrder"
    LITTLE_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
    BIG_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
    values = JavaStaticMethod("()[Ljava/nio/ByteOrder;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/ByteOrder;")
    nativeOrder = JavaStaticMethod("()Ljava/nio/ByteOrder;")
    LITTLE_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
    BIG_ENDIAN = JavaStaticField("Ljava/nio/ByteOrder;")
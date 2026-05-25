from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageDigestSpi"]

class MessageDigestSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigestSpi"
    __javaconstructor__ = [("()V", False)]
    engineGetDigestLength = JavaMethod("()I")
    engineUpdate = JavaMultipleMethod([("(B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    engineDigest = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False)])
    engineReset = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
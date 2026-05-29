from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageDigest"]

class MessageDigest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigest"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("(B)V", False, False), ("([BII)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;)Ljava/security/MessageDigest;", True, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    isEqual = JavaStaticMethod("([B[B)Z")
    digest = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False), ("([B)[B", False, False)])
    getDigestLength = JavaMethod("()I")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageDigest"]

class MessageDigest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigest"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/MessageDigest;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    update = JavaMultipleMethod([("(B)V", False, False), ("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    digest = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False), ("([B)[B", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    isEqual = JavaStaticMethod("([B[B)Z")
    reset = JavaMethod("()V")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getDigestLength = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
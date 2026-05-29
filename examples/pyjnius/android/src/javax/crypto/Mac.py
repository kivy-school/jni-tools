from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Mac"]

class Mac(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/Mac"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getMacLength = JavaMethod("()I")
    doFinal = JavaMultipleMethod([("()[B", False, False), ("([B)[B", False, False), ("([BI)V", False, False)])
    reset = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("(B)V", False, False), ("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Mac;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
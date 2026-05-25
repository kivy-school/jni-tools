from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Mac"]

class Mac(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/Mac"
    __javaconstructor__ = [("(Ljavax/crypto/MacSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Mac;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getMacLength = JavaMethod("()I")
    init = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    update = JavaMultipleMethod([("(B)V", False, False), ("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    doFinal = JavaMultipleMethod([("()[B", False, False), ("([BI)V", False, False), ("([B)[B", False, False)])
    reset = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
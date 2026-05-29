from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signature"]

class Signature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signature"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    initVerify = JavaMultipleMethod([("(Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/security/PublicKey;)V", False, False)])
    initSign = JavaMultipleMethod([("(Ljava/security/PrivateKey;)V", False, False), ("(Ljava/security/PrivateKey;Ljava/security/SecureRandom;)V", False, False)])
    setParameter = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("(B)V", False, False), ("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;)Ljava/security/Signature;", True, False)])
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    sign = JavaMultipleMethod([("([BII)I", False, False), ("()[B", False, False)])
    verify = JavaMultipleMethod([("([BII)Z", False, False), ("([B)Z", False, False)])
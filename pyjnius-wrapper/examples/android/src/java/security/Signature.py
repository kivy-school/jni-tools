from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signature"]

class Signature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signature"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    SIGN = JavaStaticField("I")
    UNINITIALIZED = JavaStaticField("I")
    VERIFY = JavaStaticField("I")
    state = JavaField("I")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/Signature;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    initVerify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/cert/Certificate;)V", False, False)])
    initSign = JavaMultipleMethod([("(Ljava/security/PrivateKey;)V", False, False), ("(Ljava/security/PrivateKey;Ljava/security/SecureRandom;)V", False, False)])
    sign = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False)])
    verify = JavaMultipleMethod([("([B)Z", False, False), ("([BII)Z", False, False)])
    update = JavaMultipleMethod([("(B)V", False, False), ("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    setParameter = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    clone = JavaMethod("()Ljava/lang/Object;")
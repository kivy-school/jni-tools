from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExemptionMechanism"]

class ExemptionMechanism(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanism"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    isCryptoAllowed = JavaMethod("(Ljava/security/Key;)Z")
    getOutputSize = JavaMethod("(I)I")
    getName = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/ExemptionMechanism;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;)V", False, False)])
    genExemptionBlob = JavaMultipleMethod([("([BI)I", False, False), ("([B)I", False, False), ("()[B", False, False)])
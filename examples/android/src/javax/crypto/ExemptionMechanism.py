from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExemptionMechanism"]

class ExemptionMechanism(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanism"
    __javaconstructor__ = [("(Ljavax/crypto/ExemptionMechanismSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/ExemptionMechanism;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    isCryptoAllowed = JavaMethod("(Ljava/security/Key;)Z")
    getOutputSize = JavaMethod("(I)I")
    init = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False)])
    genExemptionBlob = JavaMultipleMethod([("()[B", False, False), ("([B)I", False, False), ("([BI)I", False, False)])
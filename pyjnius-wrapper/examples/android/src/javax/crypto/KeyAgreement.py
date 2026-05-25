from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyAgreement"]

class KeyAgreement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyAgreement"
    __javaconstructor__ = [("(Ljavax/crypto/KeyAgreementSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/KeyAgreement;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyAgreement;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/KeyAgreement;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    doPhase = JavaMethod("(Ljava/security/Key;Z)Ljava/security/Key;")
    generateSecret = JavaMultipleMethod([("()[B", False, False), ("([BI)I", False, False), ("(Ljava/lang/String;)Ljavax/crypto/SecretKey;", False, False)])
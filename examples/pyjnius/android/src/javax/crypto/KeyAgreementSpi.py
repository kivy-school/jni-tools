from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyAgreementSpi"]

class KeyAgreementSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyAgreementSpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(Ljava/security/Key;Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    engineDoPhase = JavaMethod("(Ljava/security/Key;Z)Ljava/security/Key;")
    engineGenerateSecret = JavaMultipleMethod([("()[B", False, False), ("([BI)I", False, False), ("(Ljava/lang/String;)Ljavax/crypto/SecretKey;", False, False)])
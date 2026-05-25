from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPairGeneratorSpi"]

class KeyPairGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPairGeneratorSpi"
    __javaconstructor__ = [("()V", False)]
    initialize = JavaMultipleMethod([("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    generateKeyPair = JavaMethod("()Ljava/security/KeyPair;")
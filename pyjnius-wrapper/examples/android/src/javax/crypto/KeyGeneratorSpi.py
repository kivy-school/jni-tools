from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyGeneratorSpi"]

class KeyGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGeneratorSpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False)])
    engineGenerateKey = JavaMethod("()Ljavax/crypto/SecretKey;")
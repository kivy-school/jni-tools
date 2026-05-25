from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyGenerator"]

class KeyGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGenerator"
    __javaconstructor__ = [("(Ljavax/crypto/KeyGeneratorSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/KeyGenerator;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False)])
    generateKey = JavaMethod("()Ljavax/crypto/SecretKey;")
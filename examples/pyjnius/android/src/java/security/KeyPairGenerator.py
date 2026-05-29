from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPairGenerator"]

class KeyPairGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPairGenerator"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyPairGenerator;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    initialize = JavaMultipleMethod([("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    genKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    generateKeyPair = JavaMethod("()Ljava/security/KeyPair;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPairGenerator"]

class KeyPairGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPairGenerator"
    generateKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False)])
    initialize = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(I)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    genKeyPair = JavaMethod("()Ljava/security/KeyPair;")
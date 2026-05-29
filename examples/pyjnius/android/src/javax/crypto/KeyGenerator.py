from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyGenerator"]

class KeyGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGenerator"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/SecureRandom;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    generateKey = JavaMethod("()Ljavax/crypto/SecretKey;")
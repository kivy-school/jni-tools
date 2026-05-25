from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKeyFactory"]

class SecretKeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactory"
    __javaconstructor__ = [("(Ljavax/crypto/SecretKeyFactorySpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/SecretKeyFactory;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    generateSecret = JavaMethod("(Ljava/security/spec/KeySpec;)Ljavax/crypto/SecretKey;")
    getKeySpec = JavaMethod("(Ljavax/crypto/SecretKey;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljavax/crypto/SecretKey;)Ljavax/crypto/SecretKey;")
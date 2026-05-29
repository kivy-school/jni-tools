from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKeyFactory"]

class SecretKeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    generateSecret = JavaMethod("(Ljava/security/spec/KeySpec;)Ljavax/crypto/SecretKey;")
    getKeySpec = JavaMethod("(Ljavax/crypto/SecretKey;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljavax/crypto/SecretKey;)Ljavax/crypto/SecretKey;")
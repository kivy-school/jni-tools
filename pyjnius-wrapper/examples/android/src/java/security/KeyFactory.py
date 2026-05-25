from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyFactory"]

class KeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactory"
    __javaconstructor__ = [("(Ljava/security/KeyFactorySpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyFactory;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    generatePublic = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PublicKey;")
    generatePrivate = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PrivateKey;")
    getKeySpec = JavaMethod("(Ljava/security/Key;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljava/security/Key;)Ljava/security/Key;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyFactory"]

class KeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyFactory;", True, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    generatePublic = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PublicKey;")
    generatePrivate = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PrivateKey;")
    getKeySpec = JavaMethod("(Ljava/security/Key;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljava/security/Key;)Ljava/security/Key;")
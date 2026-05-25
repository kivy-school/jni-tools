from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyFactorySpi"]

class KeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineGeneratePublic = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PublicKey;")
    engineGeneratePrivate = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PrivateKey;")
    engineGetKeySpec = JavaMethod("(Ljava/security/Key;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    engineTranslateKey = JavaMethod("(Ljava/security/Key;)Ljava/security/Key;")
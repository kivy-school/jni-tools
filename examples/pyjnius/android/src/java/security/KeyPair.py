from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPair"]

class KeyPair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPair"
    __javaconstructor__ = [("(Ljava/security/PublicKey;Ljava/security/PrivateKey;)V", False)]
    getPublic = JavaMethod("()Ljava/security/PublicKey;")
    getPrivate = JavaMethod("()Ljava/security/PrivateKey;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signer"]

class Signer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signer"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False)]
    getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    setKeyPair = JavaMethod("(Ljava/security/KeyPair;)V")
    toString = JavaMethod("()Ljava/lang/String;")
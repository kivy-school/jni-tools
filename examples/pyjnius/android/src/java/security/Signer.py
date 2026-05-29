from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signer"]

class Signer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signer"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False), ("(Ljava/lang/String;)V", False)]
    getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    toString = JavaMethod("()Ljava/lang/String;")
    setKeyPair = JavaMethod("(Ljava/security/KeyPair;)V")
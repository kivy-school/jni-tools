from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Identity"]

class Identity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Identity"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False), ("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getScope = JavaMethod("()Ljava/security/IdentityScope;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    setPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    setInfo = JavaMethod("(Ljava/lang/String;)V")
    getInfo = JavaMethod("()Ljava/lang/String;")
    addCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    removeCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    certificates = JavaMethod("()[Ljava/security/Certificate;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    identityEquals = JavaMethod("(Ljava/security/Identity;)Z")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Z)Ljava/lang/String;", False, False)])
    hashCode = JavaMethod("()I")
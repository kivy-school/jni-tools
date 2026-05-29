from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Identity"]

class Identity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Identity"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False)]
    certificates = JavaMethod("()[Ljava/security/Certificate;")
    getInfo = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Z)Ljava/lang/String;", False, False)])
    hashCode = JavaMethod("()I")
    getScope = JavaMethod("()Ljava/security/IdentityScope;")
    setPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    setInfo = JavaMethod("(Ljava/lang/String;)V")
    addCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    removeCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXCertPathValidatorResult"]

class PKIXCertPathValidatorResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathValidatorResult"
    __javaconstructor__ = [("(Ljava/security/cert/TrustAnchor;Ljava/security/cert/PolicyNode;Ljava/security/PublicKey;)V", False)]
    getTrustAnchor = JavaMethod("()Ljava/security/cert/TrustAnchor;")
    getPolicyTree = JavaMethod("()Ljava/security/cert/PolicyNode;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
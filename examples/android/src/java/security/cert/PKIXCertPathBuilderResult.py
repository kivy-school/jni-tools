from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXCertPathBuilderResult"]

class PKIXCertPathBuilderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathBuilderResult"
    __javaconstructor__ = [("(Ljava/security/cert/CertPath;Ljava/security/cert/TrustAnchor;Ljava/security/cert/PolicyNode;Ljava/security/PublicKey;)V", False)]
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    toString = JavaMethod("()Ljava/lang/String;")
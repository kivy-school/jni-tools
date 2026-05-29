from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathTrustManagerParameters"]

class CertPathTrustManagerParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/CertPathTrustManagerParameters"
    __javaconstructor__ = [("(Ljava/security/cert/CertPathParameters;)V", False)]
    getParameters = JavaMethod("()Ljava/security/cert/CertPathParameters;")
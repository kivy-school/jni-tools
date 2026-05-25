from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathBuilderSpi"]

class CertPathBuilderSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderSpi"
    __javaconstructor__ = [("()V", False)]
    engineBuild = JavaMethod("(Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathBuilderResult;")
    engineGetRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
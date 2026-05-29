from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidatorSpi"]

class CertPathValidatorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorSpi"
    __javaconstructor__ = [("()V", False)]
    engineValidate = JavaMethod("(Ljava/security/cert/CertPath;Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathValidatorResult;")
    engineGetRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidator"]

class CertPathValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidator"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    validate = JavaMethod("(Ljava/security/cert/CertPath;Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathValidatorResult;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
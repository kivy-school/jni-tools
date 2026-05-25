from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidator"]

class CertPathValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidator"
    __javaconstructor__ = [("(Ljava/security/cert/CertPathValidatorSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathValidator;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    validate = JavaMethod("(Ljava/security/cert/CertPath;Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathValidatorResult;")
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
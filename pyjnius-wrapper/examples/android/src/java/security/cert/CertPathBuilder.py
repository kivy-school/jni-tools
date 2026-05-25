from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathBuilder"]

class CertPathBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilder"
    __javaconstructor__ = [("(Ljava/security/cert/CertPathBuilderSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathBuilder;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    build = JavaMethod("(Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathBuilderResult;")
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
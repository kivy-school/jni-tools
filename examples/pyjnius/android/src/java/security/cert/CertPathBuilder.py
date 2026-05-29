from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathBuilder"]

class CertPathBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilder"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathBuilder;", True, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    build = JavaMethod("(Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathBuilderResult;")
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
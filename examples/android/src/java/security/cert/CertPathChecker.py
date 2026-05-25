from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathChecker"]

class CertPathChecker(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathChecker"
    init = JavaMethod("(Z)V")
    isForwardCheckingSupported = JavaMethod("()Z")
    check = JavaMethod("(Ljava/security/cert/Certificate;)V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathChecker"]

class CertPathChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathChecker"
    init = JavaMethod("(Z)V")
    isForwardCheckingSupported = JavaMethod("()Z")
    check = JavaMethod("(Ljava/security/cert/Certificate;)V")
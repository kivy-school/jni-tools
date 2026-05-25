from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXCertPathChecker"]

class PKIXCertPathChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathChecker"
    __javaconstructor__ = [("()V", False)]
    init = JavaMethod("(Z)V")
    isForwardCheckingSupported = JavaMethod("()Z")
    getSupportedExtensions = JavaMethod("()Ljava/util/Set;")
    check = JavaMultipleMethod([("(Ljava/security/cert/Certificate;Ljava/util/Collection;)V", False, False), ("(Ljava/security/cert/Certificate;)V", False, False)])
    clone = JavaMethod("()Ljava/lang/Object;")
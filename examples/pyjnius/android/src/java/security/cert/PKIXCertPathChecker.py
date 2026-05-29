from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXCertPathChecker"]

class PKIXCertPathChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathChecker"
    getSupportedExtensions = JavaMethod("()Ljava/util/Set;")
    clone = JavaMethod("()Ljava/lang/Object;")
    init = JavaMethod("(Z)V")
    isForwardCheckingSupported = JavaMethod("()Z")
    check = JavaMultipleMethod([("(Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/security/cert/Certificate;Ljava/util/Collection;)V", False, False)])
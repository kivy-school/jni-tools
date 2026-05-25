from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidatorResult"]

class CertPathValidatorResult(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorResult"
    clone = JavaMethod("()Ljava/lang/Object;")
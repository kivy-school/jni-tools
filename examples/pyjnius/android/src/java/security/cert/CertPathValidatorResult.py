from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidatorResult"]

class CertPathValidatorResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorResult"
    clone = JavaMethod("()Ljava/lang/Object;")
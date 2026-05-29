from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathBuilderResult"]

class CertPathBuilderResult(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderResult"
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    clone = JavaMethod("()Ljava/lang/Object;")
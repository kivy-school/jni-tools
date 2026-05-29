from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathBuilderResult"]

class CertPathBuilderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderResult"
    clone = JavaMethod("()Ljava/lang/Object;")
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathParameters"]

class CertPathParameters(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathParameters"
    clone = JavaMethod("()Ljava/lang/Object;")
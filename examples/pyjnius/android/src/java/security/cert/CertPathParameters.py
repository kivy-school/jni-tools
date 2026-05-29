from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathParameters"]

class CertPathParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathParameters"
    clone = JavaMethod("()Ljava/lang/Object;")
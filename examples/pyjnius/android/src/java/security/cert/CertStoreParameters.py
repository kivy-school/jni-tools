from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertStoreParameters"]

class CertStoreParameters(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreParameters"
    clone = JavaMethod("()Ljava/lang/Object;")
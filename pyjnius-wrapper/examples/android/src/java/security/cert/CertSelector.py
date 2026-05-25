from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertSelector"]

class CertSelector(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertSelector"
    match = JavaMethod("(Ljava/security/cert/Certificate;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
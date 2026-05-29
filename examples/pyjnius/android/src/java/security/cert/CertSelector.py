from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertSelector"]

class CertSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertSelector"
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/Certificate;)Z")
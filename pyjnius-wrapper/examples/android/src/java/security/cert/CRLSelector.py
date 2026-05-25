from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRLSelector"]

class CRLSelector(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLSelector"
    match = JavaMethod("(Ljava/security/cert/CRL;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
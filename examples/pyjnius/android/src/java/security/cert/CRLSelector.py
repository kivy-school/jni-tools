from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRLSelector"]

class CRLSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLSelector"
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/CRL;)Z")
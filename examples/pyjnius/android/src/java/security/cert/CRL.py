from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRL"]

class CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRL"
    isRevoked = JavaMethod("(Ljava/security/cert/Certificate;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
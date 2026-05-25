from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRL"]

class CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRL"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getType = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    isRevoked = JavaMethod("(Ljava/security/cert/Certificate;)Z")
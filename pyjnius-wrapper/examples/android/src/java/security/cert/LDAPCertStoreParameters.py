from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LDAPCertStoreParameters"]

class LDAPCertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/LDAPCertStoreParameters"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getServerName = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
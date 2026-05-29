from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClientCertRequest"]

class ClientCertRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ClientCertRequest"
    __javaconstructor__ = [("()V", False)]
    getPrincipals = JavaMethod("()[Ljava/security/Principal;")
    cancel = JavaMethod("()V")
    ignore = JavaMethod("()V")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getKeyTypes = JavaMethod("()[Ljava/lang/String;")
    proceed = JavaMethod("(Ljava/security/PrivateKey;[Ljava/security/cert/X509Certificate;)V")
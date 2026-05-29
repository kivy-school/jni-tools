from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClientCertRequest"]

class ClientCertRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ClientCertRequest"
    __javaconstructor__ = [("()V", False)]
    getKeyTypes = JavaMethod("()[Ljava/lang/String;")
    getPrincipals = JavaMethod("()[Ljava/security/Principal;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    proceed = JavaMethod("(Ljava/security/PrivateKey;[Ljava/security/cert/X509Certificate;)V")
    ignore = JavaMethod("()V")
    cancel = JavaMethod("()V")
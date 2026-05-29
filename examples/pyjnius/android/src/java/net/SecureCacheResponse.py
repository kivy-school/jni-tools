from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureCacheResponse"]

class SecureCacheResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SecureCacheResponse"
    __javaconstructor__ = [("()V", False)]
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getLocalCertificateChain = JavaMethod("()Ljava/util/List;")
    getServerCertificateChain = JavaMethod("()Ljava/util/List;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getSSLSession = JavaMethod("()Ljava/util/Optional;")
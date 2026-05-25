from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSession"]

class SSLSession(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSession"
    getId = JavaMethod("()[B")
    getSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getCreationTime = JavaMethod("()J")
    getLastAccessedTime = JavaMethod("()J")
    invalidate = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    putValue = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getValue = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    removeValue = JavaMethod("(Ljava/lang/String;)V")
    getValueNames = JavaMethod("()[Ljava/lang/String;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getPeerHost = JavaMethod("()Ljava/lang/String;")
    getPeerPort = JavaMethod("()I")
    getPacketBufferSize = JavaMethod("()I")
    getApplicationBufferSize = JavaMethod("()I")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSession"]

class SSLSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSession"
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getId = JavaMethod("()[B")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    isValid = JavaMethod("()Z")
    putValue = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    invalidate = JavaMethod("()V")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getLastAccessedTime = JavaMethod("()J")
    removeValue = JavaMethod("(Ljava/lang/String;)V")
    getValueNames = JavaMethod("()[Ljava/lang/String;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getPacketBufferSize = JavaMethod("()I")
    getApplicationBufferSize = JavaMethod("()I")
    getPeerHost = JavaMethod("()Ljava/lang/String;")
    getPeerPort = JavaMethod("()I")
    getCreationTime = JavaMethod("()J")
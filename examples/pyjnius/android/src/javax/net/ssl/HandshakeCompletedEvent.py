from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandshakeCompletedEvent"]

class HandshakeCompletedEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedEvent"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSocket;Ljavax/net/ssl/SSLSession;)V", False)]
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getSocket = JavaMethod("()Ljavax/net/ssl/SSLSocket;")
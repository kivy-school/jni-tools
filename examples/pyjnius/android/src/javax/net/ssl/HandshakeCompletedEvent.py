from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandshakeCompletedEvent"]

class HandshakeCompletedEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedEvent"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSocket;Ljavax/net/ssl/SSLSession;)V", False)]
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getSocket = JavaMethod("()Ljavax/net/ssl/SSLSocket;")
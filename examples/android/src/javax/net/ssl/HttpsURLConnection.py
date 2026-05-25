from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpsURLConnection"]

class HttpsURLConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HttpsURLConnection"
    __javaconstructor__ = [("(Ljava/net/URL;)V", False)]
    hostnameVerifier = JavaField("Ljavax/net/ssl/HostnameVerifier;")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getServerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    setDefaultHostnameVerifier = JavaStaticMethod("(Ljavax/net/ssl/HostnameVerifier;)V")
    getDefaultHostnameVerifier = JavaStaticMethod("()Ljavax/net/ssl/HostnameVerifier;")
    setHostnameVerifier = JavaMethod("(Ljavax/net/ssl/HostnameVerifier;)V")
    getHostnameVerifier = JavaMethod("()Ljavax/net/ssl/HostnameVerifier;")
    setDefaultSSLSocketFactory = JavaStaticMethod("(Ljavax/net/ssl/SSLSocketFactory;)V")
    getDefaultSSLSocketFactory = JavaStaticMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    setSSLSocketFactory = JavaMethod("(Ljavax/net/ssl/SSLSocketFactory;)V")
    getSSLSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
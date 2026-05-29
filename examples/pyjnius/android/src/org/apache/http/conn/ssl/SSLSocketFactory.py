from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSocketFactory"]

class SSLSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/SSLSocketFactory"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/KeyStore;Ljava/lang/String;Ljava/security/KeyStore;Ljava/security/SecureRandom;Lorg/apache/http/conn/scheme/HostNameResolver;)V", False), ("(Ljava/security/KeyStore;)V", False), ("(Ljava/security/KeyStore;Ljava/lang/String;)V", False), ("(Ljava/security/KeyStore;Ljava/lang/String;Ljava/security/KeyStore;)V", False)]
    ALLOW_ALL_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    SSL = JavaStaticField("Ljava/lang/String;")
    SSLV2 = JavaStaticField("Ljava/lang/String;")
    STRICT_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    TLS = JavaStaticField("Ljava/lang/String;")
    getSocketFactory = JavaStaticMethod("()Lorg/apache/http/conn/ssl/SSLSocketFactory;")
    createSocket = JavaMultipleMethod([("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False)])
    connectSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;ILjava/net/InetAddress;ILorg/apache/http/params/HttpParams;)Ljava/net/Socket;")
    isSecure = JavaMethod("(Ljava/net/Socket;)Z")
    setHostnameVerifier = JavaMethod("(Lorg/apache/http/conn/ssl/X509HostnameVerifier;)V")
    getHostnameVerifier = JavaMethod("()Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
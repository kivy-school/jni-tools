from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SSLSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/SSLSocketFactory"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/KeyStore;Ljava/lang/String;Ljava/security/KeyStore;Ljava/security/SecureRandom;Lorg/apache/http/conn/scheme/HostNameResolver;)V", False), ("(Ljava/security/KeyStore;)V", False), ("(Ljava/security/KeyStore;Ljava/lang/String;)V", False), ("(Ljava/security/KeyStore;Ljava/lang/String;Ljava/security/KeyStore;)V", False)]
    ALLOW_ALL_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    SSL = JavaStaticField("Ljava/lang/String;")
    SSLV2 = JavaStaticField("Ljava/lang/String;")
    STRICT_HOSTNAME_VERIFIER = JavaStaticField("Lorg/apache/http/conn/ssl/X509HostnameVerifier;")
    TLS = JavaStaticField("Ljava/lang/String;")
    connectSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;ILjava/net/InetAddress;ILorg/apache/http/params/HttpParams;)Ljava/net/Socket;")
    getSocketFactory = JavaStaticMethod("()Lorg/apache/http/conn/ssl/SSLSocketFactory;")
    createSocket = JavaMultipleMethod([("()Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False)])
    isSecure = JavaMethod("(Ljava/net/Socket;)Z")
    setHostnameVerifier = JavaMethod("(Lorg/apache/http/conn/ssl/X509HostnameVerifier;)V")
    getHostnameVerifier = JavaMethod("()Lorg/apache/http/conn/ssl/X509HostnameVerifier;")

class AllowAllHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/AllowAllHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")

class AbstractVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/AbstractVerifier"
    __javaconstructor__ = [("()V", False)]
    getCNs = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    acceptableCountryWildcard = JavaStaticMethod("(Ljava/lang/String;)Z")
    countDots = JavaStaticMethod("(Ljava/lang/String;)I")
    getDNSSubjectAlts = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    verify = JavaMultipleMethod([("(Ljava/lang/String;Ljavax/net/ssl/SSLSocket;)V", False, False), ("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z", False, False), ("(Ljava/lang/String;Ljava/security/cert/X509Certificate;)V", False, False), ("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;Z)V", False, False)])

class StrictHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/StrictHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")

class X509HostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/X509HostnameVerifier"
    verify = JavaMultipleMethod([("(Ljava/lang/String;Ljavax/net/ssl/SSLSocket;)V", False, False), ("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z", False, False), ("(Ljava/lang/String;Ljava/security/cert/X509Certificate;)V", False, False), ("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V", False, False)])

class BrowserCompatHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/BrowserCompatHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")
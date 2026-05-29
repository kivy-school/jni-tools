from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLContext"]

class SSLContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContext"
    getSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getDefault = JavaStaticMethod("()Ljavax/net/ssl/SSLContext;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False)])
    init = JavaMethod("([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    setDefault = JavaStaticMethod("(Ljavax/net/ssl/SSLContext;)V")
    getServerSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLServerSocketFactory;")
    createSSLEngine = JavaMultipleMethod([("(Ljava/lang/String;I)Ljavax/net/ssl/SSLEngine;", False, False), ("()Ljavax/net/ssl/SSLEngine;", False, False)])
    getServerSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getClientSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getDefaultSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    getSupportedSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
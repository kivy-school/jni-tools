from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLContext"]

class SSLContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContext"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLContextSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getDefault = JavaStaticMethod("()Ljavax/net/ssl/SSLContext;")
    setDefault = JavaStaticMethod("(Ljavax/net/ssl/SSLContext;)V")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/SSLContext;", True, False)])
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMethod("([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V")
    getSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    getServerSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLServerSocketFactory;")
    createSSLEngine = JavaMultipleMethod([("()Ljavax/net/ssl/SSLEngine;", False, False), ("(Ljava/lang/String;I)Ljavax/net/ssl/SSLEngine;", False, False)])
    getServerSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getClientSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getDefaultSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    getSupportedSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
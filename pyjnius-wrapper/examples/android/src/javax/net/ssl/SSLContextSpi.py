from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLContextSpi"]

class SSLContextSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContextSpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMethod("([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V")
    engineGetSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    engineGetServerSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLServerSocketFactory;")
    engineCreateSSLEngine = JavaMultipleMethod([("()Ljavax/net/ssl/SSLEngine;", False, False), ("(Ljava/lang/String;I)Ljavax/net/ssl/SSLEngine;", False, False)])
    engineGetServerSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    engineGetClientSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    engineGetDefaultSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    engineGetSupportedSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
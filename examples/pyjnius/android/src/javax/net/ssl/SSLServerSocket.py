from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLServerSocket"]

class SSLServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocket"
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")
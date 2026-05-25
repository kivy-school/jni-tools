from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLServerSocket"]

class SSLServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocket"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(II)V", False), ("(IILjava/net/InetAddress;)V", False)]
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    setNeedClientAuth = JavaMethod("(Z)V")
    getNeedClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")
    toString = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSocket"]

class SSLSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocket"
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
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
    getHandshakeSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    addHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    removeHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    startHandshake = JavaMethod("()V")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")
    getApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    getHandshakeApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    setHandshakeApplicationProtocolSelector = JavaMethod("(Ljava/util/function/BiFunction;)V")
    getHandshakeApplicationProtocolSelector = JavaMethod("()Ljava/util/function/BiFunction;")
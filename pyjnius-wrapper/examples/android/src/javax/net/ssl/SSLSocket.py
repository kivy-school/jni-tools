from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSocket"]

class SSLSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocket"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;I)V", False), ("(Ljava/net/InetAddress;I)V", False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)V", False), ("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)V", False)]
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getHandshakeSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    addHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    removeHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    startHandshake = JavaMethod("()V")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getNeedClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")
    getApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    getHandshakeApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    setHandshakeApplicationProtocolSelector = JavaMethod("(Ljava/util/function/BiFunction;)V")
    getHandshakeApplicationProtocolSelector = JavaMethod("()Ljava/util/function/BiFunction;")
    toString = JavaMethod("()Ljava/lang/String;")
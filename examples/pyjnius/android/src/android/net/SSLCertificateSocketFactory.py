from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLCertificateSocketFactory"]

class SSLCertificateSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/SSLCertificateSocketFactory"
    __javaconstructor__ = [("(I)V", False)]
    setNpnProtocols = JavaMethod("([[B)V")
    setKeyManagers = JavaMethod("([Ljavax/net/ssl/KeyManager;)V")
    setHostname = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;)V")
    createSocket = JavaMultipleMethod([("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False)])
    getInsecure = JavaStaticMethod("(ILandroid/net/SSLSessionCache;)Ljavax/net/ssl/SSLSocketFactory;")
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getNpnSelectedProtocol = JavaMethod("(Ljava/net/Socket;)[B")
    setTrustManagers = JavaMethod("([Ljavax/net/ssl/TrustManager;)V")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    setUseSessionTickets = JavaMethod("(Ljava/net/Socket;Z)V")
    getDefault = JavaMultipleMethod([("(ILandroid/net/SSLSessionCache;)Ljavax/net/ssl/SSLSocketFactory;", True, False), ("(I)Ljavax/net/SocketFactory;", True, False)])
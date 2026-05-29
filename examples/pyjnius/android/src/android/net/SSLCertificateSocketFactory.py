from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLCertificateSocketFactory"]

class SSLCertificateSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/SSLCertificateSocketFactory"
    __javaconstructor__ = [("(I)V", False)]
    getDefault = JavaMultipleMethod([("(I)Ljavax/net/SocketFactory;", True, False), ("(ILandroid/net/SSLSessionCache;)Ljavax/net/ssl/SSLSocketFactory;", True, False)])
    getInsecure = JavaStaticMethod("(ILandroid/net/SSLSessionCache;)Ljavax/net/ssl/SSLSocketFactory;")
    setTrustManagers = JavaMethod("([Ljavax/net/ssl/TrustManager;)V")
    setNpnProtocols = JavaMethod("([[B)V")
    getNpnSelectedProtocol = JavaMethod("(Ljava/net/Socket;)[B")
    setKeyManagers = JavaMethod("([Ljavax/net/ssl/KeyManager;)V")
    setUseSessionTickets = JavaMethod("(Ljava/net/Socket;Z)V")
    setHostname = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;)V")
    createSocket = JavaMultipleMethod([("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False)])
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
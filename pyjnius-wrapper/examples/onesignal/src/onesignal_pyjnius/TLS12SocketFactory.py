from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TLS12SocketFactory"]

class TLS12SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/TLS12SocketFactory"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSocketFactory;)V", False)]
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    createSocket = JavaMultipleMethod([("()Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False)])
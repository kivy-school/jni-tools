from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSocketFactory"]

class SSLSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocketFactory"
    __javaconstructor__ = [("()V", False)]
    createSocket = JavaMultipleMethod([("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/io/InputStream;Z)Ljava/net/Socket;", False, False)])
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getDefault = JavaStaticMethod("()Ljavax/net/SocketFactory;")
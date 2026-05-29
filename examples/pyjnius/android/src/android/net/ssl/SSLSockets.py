from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSockets"]

class SSLSockets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ssl/SSLSockets"
    isSupportedSocket = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;)Z")
    exportKeyingMaterial = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;Ljava/lang/String;[BI)[B")
    setUseSessionTickets = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;Z)V")
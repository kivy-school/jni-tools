from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SSLSockets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ssl/SSLSockets"
    isSupportedSocket = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;)Z")
    setUseSessionTickets = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;Z)V")
    exportKeyingMaterial = JavaStaticMethod("(Ljavax/net/ssl/SSLSocket;Ljava/lang/String;[BI)[B")

class SSLEngines(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ssl/SSLEngines"
    setUseSessionTickets = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Z)V")
    exportKeyingMaterial = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Ljava/lang/String;[BI)[B")
    isSupportedEngine = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;)Z")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LayeredSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/LayeredSocketFactory"
    createSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;")

class SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/SocketFactory"
    connectSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;ILjava/net/InetAddress;ILorg/apache/http/params/HttpParams;)Ljava/net/Socket;")
    createSocket = JavaMethod("()Ljava/net/Socket;")
    isSecure = JavaMethod("(Ljava/net/Socket;)Z")

class HostNameResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/HostNameResolver"
    resolve = JavaMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")
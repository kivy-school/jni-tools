from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketFactory"]

class SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/SocketFactory"
    createSocket = JavaMethod("()Ljava/net/Socket;")
    connectSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;ILjava/net/InetAddress;ILorg/apache/http/params/HttpParams;)Ljava/net/Socket;")
    isSecure = JavaMethod("(Ljava/net/Socket;)Z")
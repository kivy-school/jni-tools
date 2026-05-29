from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketFactory"]

class SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/SocketFactory"
    createSocket = JavaMultipleMethod([("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False)])
    getDefault = JavaStaticMethod("()Ljavax/net/SocketFactory;")
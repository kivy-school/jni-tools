from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/SocketFactory"
    createSocket = JavaMultipleMethod([("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False)])
    getDefault = JavaStaticMethod("()Ljavax/net/SocketFactory;")

class ServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ServerSocketFactory"
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")
    createServerSocket = JavaMultipleMethod([("(II)Ljava/net/ServerSocket;", False, False), ("(IILjava/net/InetAddress;)Ljava/net/ServerSocket;", False, False), ("(I)Ljava/net/ServerSocket;", False, False), ("()Ljava/net/ServerSocket;", False, False)])
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocketFactory"]

class ServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ServerSocketFactory"
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")
    createServerSocket = JavaMultipleMethod([("(II)Ljava/net/ServerSocket;", False, False), ("(IILjava/net/InetAddress;)Ljava/net/ServerSocket;", False, False), ("(I)Ljava/net/ServerSocket;", False, False), ("()Ljava/net/ServerSocket;", False, False)])
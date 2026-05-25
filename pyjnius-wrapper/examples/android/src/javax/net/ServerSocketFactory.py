from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServerSocketFactory"]

class ServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ServerSocketFactory"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")
    createServerSocket = JavaMultipleMethod([("()Ljava/net/ServerSocket;", False, False), ("(I)Ljava/net/ServerSocket;", False, False), ("(II)Ljava/net/ServerSocket;", False, False), ("(IILjava/net/InetAddress;)Ljava/net/ServerSocket;", False, False)])
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSocketFactory"]

class SSLSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocketFactory"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljavax/net/SocketFactory;")
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    createSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;")
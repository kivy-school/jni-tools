from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLServerSocketFactory"]

class SSLServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocketFactory"
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")
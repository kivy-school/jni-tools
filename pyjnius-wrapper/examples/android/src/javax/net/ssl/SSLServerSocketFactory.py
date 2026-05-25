from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLServerSocketFactory"]

class SSLServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocketFactory"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
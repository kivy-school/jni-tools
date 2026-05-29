from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManagerFactory"]

class TrustManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/TrustManagerFactory;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/KeyStore;)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getTrustManagers = JavaMethod("()[Ljavax/net/ssl/TrustManager;")
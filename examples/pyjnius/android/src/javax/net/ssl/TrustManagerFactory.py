from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManagerFactory"]

class TrustManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactory"
    __javaconstructor__ = [("(Ljavax/net/ssl/TrustManagerFactorySpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/TrustManagerFactory;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(Ljava/security/KeyStore;)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    getTrustManagers = JavaMethod("()[Ljavax/net/ssl/TrustManager;")
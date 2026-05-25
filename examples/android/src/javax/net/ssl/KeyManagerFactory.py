from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManagerFactory"]

class KeyManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactory"
    __javaconstructor__ = [("(Ljavax/net/ssl/KeyManagerFactorySpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/KeyManagerFactory;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(Ljava/security/KeyStore;[C)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    getKeyManagers = JavaMethod("()[Ljavax/net/ssl/KeyManager;")
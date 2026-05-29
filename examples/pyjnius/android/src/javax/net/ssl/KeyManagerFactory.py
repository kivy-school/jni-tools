from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManagerFactory"]

class KeyManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/KeyManagerFactory;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/KeyStore;[C)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getKeyManagers = JavaMethod("()[Ljavax/net/ssl/KeyManager;")
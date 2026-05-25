from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManagerFactorySpi"]

class TrustManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(Ljava/security/KeyStore;)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    engineGetTrustManagers = JavaMethod("()[Ljavax/net/ssl/TrustManager;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManagerFactorySpi"]

class KeyManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(Ljava/security/KeyStore;[C)V", False, False), ("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False)])
    engineGetKeyManagers = JavaMethod("()[Ljavax/net/ssl/KeyManager;")
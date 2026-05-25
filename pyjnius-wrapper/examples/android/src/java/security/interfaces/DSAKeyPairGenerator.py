from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAKeyPairGenerator"]

class DSAKeyPairGenerator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKeyPairGenerator"
    initialize = JavaMultipleMethod([("(Ljava/security/interfaces/DSAParams;Ljava/security/SecureRandom;)V", False, False), ("(IZLjava/security/SecureRandom;)V", False, False)])
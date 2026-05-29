from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAKeyPairGenerator"]

class DSAKeyPairGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKeyPairGenerator"
    initialize = JavaMultipleMethod([("(Ljava/security/interfaces/DSAParams;Ljava/security/SecureRandom;)V", False, False), ("(IZLjava/security/SecureRandom;)V", False, False)])
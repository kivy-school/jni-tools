from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherSpi"]

class CipherSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherSpi"
    __javaconstructor__ = [("()V", False)]
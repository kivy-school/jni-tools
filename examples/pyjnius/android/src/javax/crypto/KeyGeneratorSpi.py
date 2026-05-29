from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyGeneratorSpi"]

class KeyGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGeneratorSpi"
    __javaconstructor__ = [("()V", False)]
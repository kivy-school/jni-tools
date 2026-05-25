from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NullCipher"]

class NullCipher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/NullCipher"
    __javaconstructor__ = [("()V", False)]
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKeyFactorySpi"]

class SecretKeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactorySpi"
    __javaconstructor__ = [("()V", False)]
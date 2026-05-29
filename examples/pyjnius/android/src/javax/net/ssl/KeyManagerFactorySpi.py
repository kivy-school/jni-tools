from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManagerFactorySpi"]

class KeyManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManagerFactorySpi"]

class TrustManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]
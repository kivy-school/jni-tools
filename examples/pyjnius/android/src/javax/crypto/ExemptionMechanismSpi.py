from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExemptionMechanismSpi"]

class ExemptionMechanismSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanismSpi"
    __javaconstructor__ = [("()V", False)]
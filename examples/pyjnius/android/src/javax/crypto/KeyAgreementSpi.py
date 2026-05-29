from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyAgreementSpi"]

class KeyAgreementSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyAgreementSpi"
    __javaconstructor__ = [("()V", False)]
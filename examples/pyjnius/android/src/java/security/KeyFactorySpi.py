from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyFactorySpi"]

class KeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactorySpi"
    __javaconstructor__ = [("()V", False)]
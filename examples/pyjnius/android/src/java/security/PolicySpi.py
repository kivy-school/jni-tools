from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicySpi"]

class PolicySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PolicySpi"
    __javaconstructor__ = [("()V", False)]
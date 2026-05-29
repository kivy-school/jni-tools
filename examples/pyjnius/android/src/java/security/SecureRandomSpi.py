from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRandomSpi"]

class SecureRandomSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandomSpi"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
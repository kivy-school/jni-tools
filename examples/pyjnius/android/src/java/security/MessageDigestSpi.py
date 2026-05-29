from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageDigestSpi"]

class MessageDigestSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigestSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")
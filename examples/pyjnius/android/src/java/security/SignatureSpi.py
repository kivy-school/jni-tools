from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignatureSpi"]

class SignatureSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignatureSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")
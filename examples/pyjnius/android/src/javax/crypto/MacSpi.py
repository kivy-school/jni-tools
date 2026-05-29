from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MacSpi"]

class MacSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/MacSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")
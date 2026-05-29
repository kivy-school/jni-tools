from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidKeException"]

class InvalidKeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidKeException"
    __javaconstructor__ = [("(I)V", False)]
    getDhGroup = JavaMethod("()I")
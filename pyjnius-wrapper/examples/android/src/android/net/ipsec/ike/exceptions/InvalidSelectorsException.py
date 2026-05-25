from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidSelectorsException"]

class InvalidSelectorsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidSelectorsException"
    __javaconstructor__ = [("(I[B)V", False)]
    getIpSecSpi = JavaMethod("()I")
    getIpSecPacketInfo = JavaMethod("()[B")
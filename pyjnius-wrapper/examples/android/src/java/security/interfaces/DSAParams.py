from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAParams"]

class DSAParams(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAParams"
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")
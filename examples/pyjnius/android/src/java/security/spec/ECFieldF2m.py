from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECFieldF2m"]

class ECFieldF2m(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECFieldF2m"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/math/BigInteger;)V", False), ("(I[I)V", False)]
    getM = JavaMethod("()I")
    getReductionPolynomial = JavaMethod("()Ljava/math/BigInteger;")
    getMidTermsOfReductionPolynomial = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getFieldSize = JavaMethod("()I")
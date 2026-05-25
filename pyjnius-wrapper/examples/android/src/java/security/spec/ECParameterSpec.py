from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECParameterSpec"]

class ECParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECParameterSpec"
    __javaconstructor__ = [("(Ljava/security/spec/EllipticCurve;Ljava/security/spec/ECPoint;Ljava/math/BigInteger;I)V", False)]
    getCurve = JavaMethod("()Ljava/security/spec/EllipticCurve;")
    getGenerator = JavaMethod("()Ljava/security/spec/ECPoint;")
    getOrder = JavaMethod("()Ljava/math/BigInteger;")
    getCofactor = JavaMethod("()I")
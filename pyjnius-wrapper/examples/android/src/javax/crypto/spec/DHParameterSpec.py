from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHParameterSpec"]

class DHParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHParameterSpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;I)V", False)]
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")
    getL = JavaMethod("()I")
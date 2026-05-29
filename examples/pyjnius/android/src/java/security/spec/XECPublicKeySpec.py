from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPublicKeySpec"]

class XECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/XECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/math/BigInteger;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getU = JavaMethod("()Ljava/math/BigInteger;")
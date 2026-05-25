from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAKey"]

class RSAKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAKey"
    getModulus = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
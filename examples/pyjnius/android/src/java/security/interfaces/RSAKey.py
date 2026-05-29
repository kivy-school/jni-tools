from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAKey"]

class RSAKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAKey"
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getModulus = JavaMethod("()Ljava/math/BigInteger;")
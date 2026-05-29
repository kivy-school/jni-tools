from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPublicKey"]

class XECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getU = JavaMethod("()Ljava/math/BigInteger;")
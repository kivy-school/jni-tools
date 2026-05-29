from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPublicKey"]

class ECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getW = JavaMethod("()Ljava/security/spec/ECPoint;")
    getParams = JavaMultipleMethod([("()Ljava/security/spec/ECParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])
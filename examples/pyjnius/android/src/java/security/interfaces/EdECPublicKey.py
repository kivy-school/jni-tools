from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPublicKey"]

class EdECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPoint = JavaMethod("()Ljava/security/spec/EdECPoint;")
    getParams = JavaMultipleMethod([("()Ljava/security/spec/NamedParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])
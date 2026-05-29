from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPrivateKey"]

class EdECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getBytes = JavaMethod("()Ljava/util/Optional;")
    getParams = JavaMultipleMethod([("()Ljava/security/spec/NamedParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])
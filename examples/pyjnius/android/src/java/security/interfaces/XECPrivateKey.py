from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPrivateKey"]

class XECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getScalar = JavaMethod("()Ljava/util/Optional;")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
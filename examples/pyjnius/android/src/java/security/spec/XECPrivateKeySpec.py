from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPrivateKeySpec"]

class XECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/XECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/AlgorithmParameterSpec;[B)V", False)]
    getScalar = JavaMethod("()[B")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
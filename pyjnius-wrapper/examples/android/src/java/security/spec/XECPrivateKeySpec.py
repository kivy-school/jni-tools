from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPrivateKeySpec"]

class XECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/XECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/AlgorithmParameterSpec;[B)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getScalar = JavaMethod("()[B")
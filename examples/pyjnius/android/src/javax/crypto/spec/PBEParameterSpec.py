from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PBEParameterSpec"]

class PBEParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PBEParameterSpec"
    __javaconstructor__ = [("([BI)V", False), ("([BILjava/security/spec/AlgorithmParameterSpec;)V", False)]
    getParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")
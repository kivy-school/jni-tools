from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExemptionMechanismSpi"]

class ExemptionMechanismSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanismSpi"
    __javaconstructor__ = [("()V", False)]
    engineGetOutputSize = JavaMethod("(I)I")
    engineInit = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False)])
    engineGenExemptionBlob = JavaMultipleMethod([("()[B", False, False), ("([BI)I", False, False)])
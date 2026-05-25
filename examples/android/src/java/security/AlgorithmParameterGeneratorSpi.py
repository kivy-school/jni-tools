from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameterGeneratorSpi"]

class AlgorithmParameterGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGeneratorSpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    engineGenerateParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
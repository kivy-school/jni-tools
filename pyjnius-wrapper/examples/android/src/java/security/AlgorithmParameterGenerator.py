from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameterGenerator"]

class AlgorithmParameterGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGenerator"
    __javaconstructor__ = [("(Ljava/security/AlgorithmParameterGeneratorSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameterGenerator;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])
    generateParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
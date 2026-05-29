from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameterGenerator"]

class AlgorithmParameterGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGenerator"
    generateParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
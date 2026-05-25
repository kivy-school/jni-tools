from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameters"]

class AlgorithmParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameters"
    __javaconstructor__ = [("(Ljava/security/AlgorithmParametersSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameters;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("([B)V", False, False), ("([BLjava/lang/String;)V", False, False)])
    getParameterSpec = JavaMethod("(Ljava/lang/Class;)Ljava/security/spec/AlgorithmParameterSpec;")
    getEncoded = JavaMultipleMethod([("()[B", False, False), ("(Ljava/lang/String;)[B", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
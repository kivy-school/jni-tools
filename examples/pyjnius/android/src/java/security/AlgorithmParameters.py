from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameters"]

class AlgorithmParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameters"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getParameterSpec = JavaMethod("(Ljava/lang/Class;)Ljava/security/spec/AlgorithmParameterSpec;")
    toString = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameters;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("([BLjava/lang/String;)V", False, False), ("([B)V", False, False)])
    getEncoded = JavaMultipleMethod([("(Ljava/lang/String;)[B", False, False), ("()[B", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParametersSpi"]

class AlgorithmParametersSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParametersSpi"
    __javaconstructor__ = [("()V", False)]
    engineInit = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("([B)V", False, False), ("([BLjava/lang/String;)V", False, False)])
    engineGetParameterSpec = JavaMethod("(Ljava/lang/Class;)Ljava/security/spec/AlgorithmParameterSpec;")
    engineGetEncoded = JavaMultipleMethod([("()[B", False, False), ("(Ljava/lang/String;)[B", False, False)])
    engineToString = JavaMethod("()Ljava/lang/String;")
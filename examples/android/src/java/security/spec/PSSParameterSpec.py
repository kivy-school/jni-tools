from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PSSParameterSpec"]

class PSSParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/PSSParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;II)V", False), ("(I)V", False)]
    DEFAULT = JavaStaticField("Ljava/security/spec/PSSParameterSpec;")
    TRAILER_FIELD_BC = JavaStaticField("I")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getSaltLength = JavaMethod("()I")
    getTrailerField = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
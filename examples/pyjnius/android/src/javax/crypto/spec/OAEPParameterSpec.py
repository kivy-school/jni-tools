from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OAEPParameterSpec"]

class OAEPParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/OAEPParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;Ljavax/crypto/spec/PSource;)V", False)]
    DEFAULT = JavaStaticField("Ljavax/crypto/spec/OAEPParameterSpec;")
    getPSource = JavaMethod("()Ljavax/crypto/spec/PSource;")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
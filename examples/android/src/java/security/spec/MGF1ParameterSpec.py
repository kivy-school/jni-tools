from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MGF1ParameterSpec"]

class MGF1ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/MGF1ParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    SHA1 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA384 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_384 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_512 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512_224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512_256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamedParameterSpec"]

class NamedParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/NamedParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    X25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    X448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_DSA_44 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_DSA_65 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_DSA_87 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_KEM_512 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_KEM_768 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ML_KEM_1024 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    getName = JavaMethod("()Ljava/lang/String;")
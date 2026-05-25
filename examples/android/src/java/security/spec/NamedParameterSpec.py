from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamedParameterSpec"]

class NamedParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/NamedParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    ED25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    X25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    X448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    getName = JavaMethod("()Ljava/lang/String;")
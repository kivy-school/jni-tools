from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdDSAParameterSpec"]

class EdDSAParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdDSAParameterSpec"
    __javaconstructor__ = [("(Z)V", False), ("(Z[B)V", False)]
    isPrehash = JavaMethod("()Z")
    getContext = JavaMethod("()Ljava/util/Optional;")
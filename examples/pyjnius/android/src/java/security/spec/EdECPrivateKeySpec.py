from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPrivateKeySpec"]

class EdECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/NamedParameterSpec;[B)V", False)]
    getBytes = JavaMethod("()[B")
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")
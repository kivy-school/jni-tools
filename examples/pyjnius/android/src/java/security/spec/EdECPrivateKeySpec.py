from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPrivateKeySpec"]

class EdECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/NamedParameterSpec;[B)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")
    getBytes = JavaMethod("()[B")
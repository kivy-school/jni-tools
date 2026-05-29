from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPublicKeySpec"]

class EdECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/NamedParameterSpec;Ljava/security/spec/EdECPoint;)V", False)]
    getPoint = JavaMethod("()Ljava/security/spec/EdECPoint;")
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")
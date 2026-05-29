from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPublicKeySpec"]

class ECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/ECPoint;Ljava/security/spec/ECParameterSpec;)V", False)]
    getW = JavaMethod("()Ljava/security/spec/ECPoint;")
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPrivateKeySpec"]

class ECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/security/spec/ECParameterSpec;)V", False)]
    getS = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")
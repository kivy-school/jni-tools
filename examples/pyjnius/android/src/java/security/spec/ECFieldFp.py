from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECFieldFp"]

class ECFieldFp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECFieldFp"
    __javaconstructor__ = [("(Ljava/math/BigInteger;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getFieldSize = JavaMethod("()I")
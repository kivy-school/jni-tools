from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECFieldFp"]

class ECFieldFp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECFieldFp"
    __javaconstructor__ = [("(Ljava/math/BigInteger;)V", False)]
    getFieldSize = JavaMethod("()I")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
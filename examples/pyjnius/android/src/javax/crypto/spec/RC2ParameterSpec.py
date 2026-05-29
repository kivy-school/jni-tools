from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RC2ParameterSpec"]

class RC2ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/RC2ParameterSpec"
    __javaconstructor__ = [("(I)V", False), ("(I[B)V", False), ("(I[BI)V", False)]
    getEffectiveKeyBits = JavaMethod("()I")
    getIV = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
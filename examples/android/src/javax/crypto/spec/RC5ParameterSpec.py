from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RC5ParameterSpec"]

class RC5ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/RC5ParameterSpec"
    __javaconstructor__ = [("(III)V", False), ("(III[B)V", False), ("(III[BI)V", False)]
    getVersion = JavaMethod("()I")
    getRounds = JavaMethod("()I")
    getWordSize = JavaMethod("()I")
    getIV = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GCMParameterSpec"]

class GCMParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/GCMParameterSpec"
    __javaconstructor__ = [("(I[B)V", False), ("(I[BII)V", False)]
    getIV = JavaMethod("()[B")
    getTLen = JavaMethod("()I")
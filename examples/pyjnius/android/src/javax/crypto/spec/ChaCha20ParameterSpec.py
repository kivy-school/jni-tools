from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChaCha20ParameterSpec"]

class ChaCha20ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/ChaCha20ParameterSpec"
    __javaconstructor__ = [("([BI)V", False)]
    getNonce = JavaMethod("()[B")
    getCounter = JavaMethod("()I")
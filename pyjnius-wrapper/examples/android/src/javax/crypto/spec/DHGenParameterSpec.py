from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHGenParameterSpec"]

class DHGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHGenParameterSpec"
    __javaconstructor__ = [("(II)V", False)]
    getPrimeSize = JavaMethod("()I")
    getExponentSize = JavaMethod("()I")
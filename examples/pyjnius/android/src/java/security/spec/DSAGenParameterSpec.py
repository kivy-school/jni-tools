from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAGenParameterSpec"]

class DSAGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAGenParameterSpec"
    __javaconstructor__ = [("(III)V", False), ("(II)V", False)]
    getPrimePLength = JavaMethod("()I")
    getSubprimeQLength = JavaMethod("()I")
    getSeedLength = JavaMethod("()I")
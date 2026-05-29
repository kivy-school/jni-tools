from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PBEKeySpec"]

class PBEKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PBEKeySpec"
    __javaconstructor__ = [("([C)V", False), ("([C[BI)V", False), ("([C[BII)V", False)]
    getPassword = JavaMethod("()[C")
    clearPassword = JavaMethod("()V")
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")
    getKeyLength = JavaMethod("()I")
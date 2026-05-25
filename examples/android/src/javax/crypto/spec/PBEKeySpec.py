from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PBEKeySpec"]

class PBEKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PBEKeySpec"
    __javaconstructor__ = [("([C)V", False), ("([C[BII)V", False), ("([C[BI)V", False)]
    clearPassword = JavaMethod("()V")
    getPassword = JavaMethod("()[C")
    getSalt = JavaMethod("()[B")
    getIterationCount = JavaMethod("()I")
    getKeyLength = JavaMethod("()I")
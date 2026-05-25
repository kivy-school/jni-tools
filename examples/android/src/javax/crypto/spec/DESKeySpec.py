from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DESKeySpec"]

class DESKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DESKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BI)V", False)]
    DES_KEY_LEN = JavaStaticField("I")
    getKey = JavaMethod("()[B")
    isParityAdjusted = JavaStaticMethod("([BI)Z")
    isWeak = JavaStaticMethod("([BI)Z")
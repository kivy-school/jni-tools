from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DESedeKeySpec"]

class DESedeKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DESedeKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BI)V", False)]
    DES_EDE_KEY_LEN = JavaStaticField("I")
    getKey = JavaMethod("()[B")
    isParityAdjusted = JavaStaticMethod("([BI)Z")
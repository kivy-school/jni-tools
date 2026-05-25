from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatPrecisionException"]

class IllegalFormatPrecisionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatPrecisionException"
    __javaconstructor__ = [("(I)V", False)]
    getPrecision = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
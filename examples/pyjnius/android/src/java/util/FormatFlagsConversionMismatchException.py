from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormatFlagsConversionMismatchException"]

class FormatFlagsConversionMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/FormatFlagsConversionMismatchException"
    __javaconstructor__ = [("(Ljava/lang/String;C)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFlags = JavaMethod("()Ljava/lang/String;")
    getConversion = JavaMethod("()C")
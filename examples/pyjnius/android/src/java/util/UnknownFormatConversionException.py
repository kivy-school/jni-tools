from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownFormatConversionException"]

class UnknownFormatConversionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/UnknownFormatConversionException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getConversion = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownFormatConversionException"]

class UnknownFormatConversionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/UnknownFormatConversionException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getConversion = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
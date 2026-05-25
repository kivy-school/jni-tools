from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatConversionException"]

class IllegalFormatConversionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatConversionException"
    __javaconstructor__ = [("(CLjava/lang/Class;)V", False)]
    getConversion = JavaMethod("()C")
    getArgumentClass = JavaMethod("()Ljava/lang/Class;")
    getMessage = JavaMethod("()Ljava/lang/String;")
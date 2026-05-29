from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharConversionException"]

class CharConversionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/CharConversionException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
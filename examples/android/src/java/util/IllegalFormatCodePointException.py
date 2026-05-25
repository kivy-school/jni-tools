from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatCodePointException"]

class IllegalFormatCodePointException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatCodePointException"
    __javaconstructor__ = [("(I)V", False)]
    getCodePoint = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
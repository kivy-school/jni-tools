from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatCodePointException"]

class IllegalFormatCodePointException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatCodePointException"
    __javaconstructor__ = [("(I)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getCodePoint = JavaMethod("()I")
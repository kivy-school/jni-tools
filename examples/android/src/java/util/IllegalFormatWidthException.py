from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatWidthException"]

class IllegalFormatWidthException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatWidthException"
    __javaconstructor__ = [("(I)V", False)]
    getWidth = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
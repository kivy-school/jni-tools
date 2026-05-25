from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MalformedInputException"]

class MalformedInputException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/MalformedInputException"
    __javaconstructor__ = [("(I)V", False)]
    getInputLength = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MissingFormatWidthException"]

class MissingFormatWidthException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/MissingFormatWidthException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getFormatSpecifier = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MissingFormatWidthException"]

class MissingFormatWidthException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/MissingFormatWidthException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFormatSpecifier = JavaMethod("()Ljava/lang/String;")
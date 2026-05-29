from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParseException"]

class ParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/ParseException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    getErrorOffset = JavaMethod("()I")
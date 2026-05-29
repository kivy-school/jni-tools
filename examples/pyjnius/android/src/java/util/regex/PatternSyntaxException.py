from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternSyntaxException"]

class PatternSyntaxException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/PatternSyntaxException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False)]
    getPattern = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getIndex = JavaMethod("()I")
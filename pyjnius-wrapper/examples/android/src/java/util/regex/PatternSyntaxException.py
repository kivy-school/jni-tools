from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternSyntaxException"]

class PatternSyntaxException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/PatternSyntaxException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False)]
    getIndex = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getPattern = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
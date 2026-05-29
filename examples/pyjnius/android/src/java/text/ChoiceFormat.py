from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChoiceFormat"]

class ChoiceFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/ChoiceFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("([D[Ljava/lang/String;)V", False)]
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    setChoices = JavaMethod("([D[Ljava/lang/String;)V")
    getLimits = JavaMethod("()[D")
    getFormats = JavaMethod("()[Ljava/lang/Object;")
    format = JavaMultipleMethod([("(JLjava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(DLjava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")
    nextDouble = JavaMultipleMethod([("(D)D", True, False), ("(DZ)D", True, False)])
    previousDouble = JavaStaticMethod("(D)D")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
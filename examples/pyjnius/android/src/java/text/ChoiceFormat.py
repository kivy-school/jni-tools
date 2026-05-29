from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChoiceFormat"]

class ChoiceFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/ChoiceFormat"
    __javaconstructor__ = [("([D[Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    INTEGER_FIELD = JavaStaticField("I")
    FRACTION_FIELD = JavaStaticField("I")
    setStrict = JavaMethod("(Z)V")
    setChoices = JavaMethod("([D[Ljava/lang/String;)V")
    getFormats = JavaMethod("()[Ljava/lang/Object;")
    toPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(DLjava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(JLjava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")
    nextDouble = JavaMultipleMethod([("(DZ)D", True, False), ("(D)D", True, False)])
    isStrict = JavaMethod("()Z")
    previousDouble = JavaStaticMethod("(D)D")
    getLimits = JavaMethod("()[D")
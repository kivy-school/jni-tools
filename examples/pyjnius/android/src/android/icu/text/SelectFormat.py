from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectFormat"]

class SelectFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SelectFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    format = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
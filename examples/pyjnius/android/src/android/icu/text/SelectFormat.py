from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectFormat"]

class SelectFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SelectFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    toPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    format = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
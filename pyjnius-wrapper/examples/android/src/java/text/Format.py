from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Format"]

class Format(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Format"
    __javaconstructor__ = [("()V", False)]
    format = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")
    parseObject = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)Ljava/lang/Object;", False, False)])
    clone = JavaMethod("()Ljava/lang/Object;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/Format/Field"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
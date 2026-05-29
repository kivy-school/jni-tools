from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Format"]

class Format(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Format"
    parseObject = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;", False, False)])
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/Format$Field"
        LANGUAGE = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        READING = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        INPUT_METHOD_SEGMENT = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
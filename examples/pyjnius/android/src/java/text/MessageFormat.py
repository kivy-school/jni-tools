from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageFormat"]

class MessageFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/MessageFormat"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;)V", False)]
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    setFormats = JavaMethod("([Ljava/text/Format;)V")
    getFormats = JavaMethod("()[Ljava/text/Format;")
    getFormatsByArgumentIndex = JavaMethod("()[Ljava/text/Format;")
    setFormatByArgumentIndex = JavaMethod("(ILjava/text/Format;)V")
    setFormatsByArgumentIndex = JavaMethod("([Ljava/text/Format;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", True, True), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("([Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMultipleMethod([("(Ljava/lang/String;)[Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/text/ParsePosition;)[Ljava/lang/Object;", False, False)])
    getLocale = JavaMethod("()Ljava/util/Locale;")
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    setFormat = JavaMethod("(ILjava/text/Format;)V")
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/MessageFormat$Field"
        ARGUMENT = JavaStaticField("Ljava/text/MessageFormat$Field;")
        LANGUAGE = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        READING = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        INPUT_METHOD_SEGMENT = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
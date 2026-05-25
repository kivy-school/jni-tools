from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageFormat"]

class MessageFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/MessageFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Locale;)V", False)]
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    setFormatsByArgumentIndex = JavaMethod("([Ljava/text/Format;)V")
    setFormats = JavaMethod("([Ljava/text/Format;)V")
    setFormatByArgumentIndex = JavaMethod("(ILjava/text/Format;)V")
    setFormat = JavaMethod("(ILjava/text/Format;)V")
    getFormatsByArgumentIndex = JavaMethod("()[Ljava/text/Format;")
    getFormats = JavaMethod("()[Ljava/text/Format;")
    format = JavaMultipleMethod([("([Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", True, True), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")
    parse = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)[Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)[Ljava/lang/Object;", False, False)])
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    clone = JavaMethod("()Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/MessageFormat/Field"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        ARGUMENT = JavaStaticField("Ljava/text/MessageFormat$Field;")
        readResolve = JavaMethod("()Ljava/lang/Object;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageFormat"]

class MessageFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/MessageFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)V", False), ("(Ljava/lang/String;Ljava/util/Locale;)V", False)]
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    setFormats = JavaMethod("([Ljava/text/Format;)V")
    parseToMap = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/Map;", False, False), ("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/util/Map;", False, False)])
    getFormats = JavaMethod("()[Ljava/text/Format;")
    getArgumentNames = JavaMethod("()Ljava/util/Set;")
    usesNamedArguments = JavaMethod("()Z")
    getApostropheMode = JavaMethod("()Landroid/icu/text/MessagePattern$ApostropheMode;")
    autoQuoteApostrophe = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getFormatByArgumentName = JavaMethod("(Ljava/lang/String;)Ljava/text/Format;")
    getFormatsByArgumentIndex = JavaMethod("()[Ljava/text/Format;")
    setFormatByArgumentIndex = JavaMethod("(ILjava/text/Format;)V")
    setFormatByArgumentName = JavaMethod("(Ljava/lang/String;Ljava/text/Format;)V")
    setFormatsByArgumentIndex = JavaMethod("([Ljava/text/Format;)V")
    setFormatsByArgumentName = JavaMethod("(Ljava/util/Map;)V")
    getULocale = JavaMethod("()Landroid/icu/util/ULocale;")
    toPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/icu/text/MessagePattern$ApostropheMode;)V", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;", True, False), ("(Ljava/util/Map;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("([Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", True, True), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)[Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)[Ljava/lang/Object;", False, False)])
    getLocale = JavaMethod("()Ljava/util/Locale;")
    setLocale = JavaMultipleMethod([("(Ljava/util/Locale;)V", False, False), ("(Landroid/icu/util/ULocale;)V", False, False)])
    setFormat = JavaMethod("(ILjava/text/Format;)V")
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/MessageFormat$Field"
        ARGUMENT = JavaStaticField("Landroid/icu/text/MessageFormat$Field;")
        LANGUAGE = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        READING = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        INPUT_METHOD_SEGMENT = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
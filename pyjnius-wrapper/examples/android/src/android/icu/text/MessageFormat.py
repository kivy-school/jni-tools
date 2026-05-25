from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageFormat"]

class MessageFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/MessageFormat"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)V", False)]
    setLocale = JavaMultipleMethod([("(Ljava/util/Locale;)V", False, False), ("(Landroid/icu/util/ULocale;)V", False, False)])
    getLocale = JavaMethod("()Ljava/util/Locale;")
    getULocale = JavaMethod("()Landroid/icu/util/ULocale;")
    applyPattern = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/icu/text/MessagePattern$ApostropheMode;)V", False, False)])
    getApostropheMode = JavaMethod("()Landroid/icu/text/MessagePattern$ApostropheMode;")
    toPattern = JavaMethod("()Ljava/lang/String;")
    setFormatsByArgumentIndex = JavaMethod("([Ljava/text/Format;)V")
    setFormatsByArgumentName = JavaMethod("(Ljava/util/Map;)V")
    setFormats = JavaMethod("([Ljava/text/Format;)V")
    setFormatByArgumentIndex = JavaMethod("(ILjava/text/Format;)V")
    setFormatByArgumentName = JavaMethod("(Ljava/lang/String;Ljava/text/Format;)V")
    setFormat = JavaMethod("(ILjava/text/Format;)V")
    getFormatsByArgumentIndex = JavaMethod("()[Ljava/text/Format;")
    getFormats = JavaMethod("()[Ljava/text/Format;")
    getArgumentNames = JavaMethod("()Ljava/util/Set;")
    getFormatByArgumentName = JavaMethod("(Ljava/lang/String;)Ljava/text/Format;")
    format = JavaMultipleMethod([("([Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/util/Map;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", True, True), ("(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;", True, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    usesNamedArguments = JavaMethod("()Z")
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")
    parse = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)[Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)[Ljava/lang/Object;", False, False)])
    parseToMap = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/util/Map;", False, False), ("(Ljava/lang/String;)Ljava/util/Map;", False, False)])
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    clone = JavaMethod("()Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    autoQuoteApostrophe = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/MessageFormat/Field"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        ARGUMENT = JavaStaticField("Landroid/icu/text/MessageFormat$Field;")
        readResolve = JavaMethod("()Ljava/lang/Object;")
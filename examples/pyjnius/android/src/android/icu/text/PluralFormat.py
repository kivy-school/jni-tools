from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PluralFormat"]

class PluralFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/PluralFormat"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/util/Locale;)V", False), ("(Ljava/util/Locale;Landroid/icu/text/PluralRules;)V", False), ("(Ljava/util/Locale;Landroid/icu/text/PluralRules$PluralType;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/text/PluralRules;Ljava/lang/String;)V", False), ("()V", False), ("(Landroid/icu/text/PluralRules;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;Ljava/lang/String;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules;Ljava/lang/String;)V", False)]
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    setNumberFormat = JavaMethod("(Landroid/icu/text/NumberFormat;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMultipleMethod([("(Landroid/icu/text/PluralFormat;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    format = JavaMultipleMethod([("(D)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")
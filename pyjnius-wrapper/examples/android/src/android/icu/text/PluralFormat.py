from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PluralFormat"]

class PluralFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/PluralFormat"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/text/PluralRules;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules;)V", False), ("(Ljava/util/Locale;Landroid/icu/text/PluralRules;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;)V", False), ("(Ljava/util/Locale;Landroid/icu/text/PluralRules$PluralType;)V", False), ("(Ljava/lang/String;)V", False), ("(Landroid/icu/util/ULocale;Ljava/lang/String;)V", False), ("(Landroid/icu/text/PluralRules;Ljava/lang/String;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules;Ljava/lang/String;)V", False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;Ljava/lang/String;)V", False)]
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    toPattern = JavaMethod("()Ljava/lang/String;")
    format = JavaMultipleMethod([("(D)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    setNumberFormat = JavaMethod("(Landroid/icu/text/NumberFormat;)V")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/icu/text/PluralFormat;)Z", False, False)])
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
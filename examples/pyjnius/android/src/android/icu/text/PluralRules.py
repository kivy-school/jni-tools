from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PluralRules"]

class PluralRules(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/PluralRules"
    DEFAULT = JavaStaticField("Landroid/icu/text/PluralRules;")
    KEYWORD_FEW = JavaStaticField("Ljava/lang/String;")
    KEYWORD_MANY = JavaStaticField("Ljava/lang/String;")
    KEYWORD_ONE = JavaStaticField("Ljava/lang/String;")
    KEYWORD_OTHER = JavaStaticField("Ljava/lang/String;")
    KEYWORD_TWO = JavaStaticField("Ljava/lang/String;")
    KEYWORD_ZERO = JavaStaticField("Ljava/lang/String;")
    NO_UNIQUE_VALUE = JavaStaticField("D")
    select = JavaMultipleMethod([("(Landroid/icu/number/FormattedNumberRange;)Ljava/lang/String;", False, False), ("(D)Ljava/lang/String;", False, False), ("(Landroid/icu/number/FormattedNumber;)Ljava/lang/String;", False, False)])
    createRules = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules;")
    parseDescription = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules;")
    getAllKeywordValues = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getUniqueKeywordValue = JavaMethod("(Ljava/lang/String;)D")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/icu/text/PluralRules;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getKeywords = JavaMethod("()Ljava/util/Set;")
    forLocale = JavaMultipleMethod([("(Ljava/util/Locale;Landroid/icu/text/PluralRules$PluralType;)Landroid/icu/text/PluralRules;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/PluralRules;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;)Landroid/icu/text/PluralRules;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/PluralRules;", True, False)])
    getSamples = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")

    class PluralType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/PluralRules$PluralType"
        CARDINAL = JavaStaticField("Landroid/icu/text/PluralRules$PluralType;")
        ORDINAL = JavaStaticField("Landroid/icu/text/PluralRules$PluralType;")
        values = JavaStaticMethod("()[Landroid/icu/text/PluralRules$PluralType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules$PluralType;")
        CARDINAL = JavaStaticField("Landroid/icu/text/PluralRules$PluralType;")
        ORDINAL = JavaStaticField("Landroid/icu/text/PluralRules$PluralType;")
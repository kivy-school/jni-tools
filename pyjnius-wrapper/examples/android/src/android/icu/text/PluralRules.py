from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    parseDescription = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules;")
    createRules = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules;")
    forLocale = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/PluralRules;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/PluralRules;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/PluralRules$PluralType;)Landroid/icu/text/PluralRules;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/PluralRules$PluralType;)Landroid/icu/text/PluralRules;", True, False)])
    hashCode = JavaMethod("()I")
    select = JavaMultipleMethod([("(D)Ljava/lang/String;", False, False), ("(Landroid/icu/number/FormattedNumber;)Ljava/lang/String;", False, False), ("(Landroid/icu/number/FormattedNumberRange;)Ljava/lang/String;", False, False)])
    getKeywords = JavaMethod("()Ljava/util/Set;")
    getUniqueKeywordValue = JavaMethod("(Ljava/lang/String;)D")
    getAllKeywordValues = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getSamples = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/icu/text/PluralRules;)Z", False, False)])

    class PluralType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/PluralRules/PluralType"
        values = JavaStaticMethod("()[Landroid/icu/text/PluralRules$PluralType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/PluralRules$PluralType;")
        CARDINAL = JavaStaticField("Landroid/icu/text/PluralRules/PluralType;")
        ORDINAL = JavaStaticField("Landroid/icu/text/PluralRules/PluralType;")
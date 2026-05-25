from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transliterator"]

class Transliterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Transliterator"
    FORWARD = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    transliterate = JavaMultipleMethod([("(Landroid/icu/text/Replaceable;II)I", False, False), ("(Landroid/icu/text/Replaceable;)V", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;Ljava/lang/String;)V", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;I)V", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;)V", False, False)])
    finishTransliteration = JavaMethod("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;)V")
    filteredTransliterate = JavaMethod("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;Z)V")
    getMaximumContextLength = JavaMethod("()I")
    getID = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)Ljava/lang/String;", True, False)])
    getFilter = JavaMethod("()Landroid/icu/text/UnicodeFilter;")
    setFilter = JavaMethod("(Landroid/icu/text/UnicodeFilter;)V")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/icu/text/Transliterator;", True, False), ("(Ljava/lang/String;I)Landroid/icu/text/Transliterator;", True, False)])
    createFromRules = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;I)Landroid/icu/text/Transliterator;")
    toRules = JavaMethod("(Z)Ljava/lang/String;")
    getElements = JavaMethod("()[Landroid/icu/text/Transliterator;")
    getSourceSet = JavaMethod("()Landroid/icu/text/UnicodeSet;")
    getTargetSet = JavaMethod("()Landroid/icu/text/UnicodeSet;")
    getInverse = JavaMethod("()Landroid/icu/text/Transliterator;")
    getAvailableIDs = JavaStaticMethod("()Ljava/util/Enumeration;")
    getAvailableSources = JavaStaticMethod("()Ljava/util/Enumeration;")
    getAvailableTargets = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getAvailableVariants = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/util/Enumeration;")

    class Position(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Transliterator/Position"
        __javaconstructor__ = [("()V", False), ("(III)V", False), ("(IIII)V", False), ("(Landroid/icu/text/Transliterator$Position;)V", False)]
        contextLimit = JavaField("I")
        contextStart = JavaField("I")
        limit = JavaField("I")
        start = JavaField("I")
        set = JavaMethod("(Landroid/icu/text/Transliterator$Position;)V")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        validate = JavaMethod("(I)V")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transliterator"]

class Transliterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Transliterator"
    FORWARD = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    createFromRules = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;I)Landroid/icu/text/Transliterator;")
    finishTransliteration = JavaMethod("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;)V")
    filteredTransliterate = JavaMethod("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;Z)V")
    getInverse = JavaMethod("()Landroid/icu/text/Transliterator;")
    getTargetSet = JavaMethod("()Landroid/icu/text/UnicodeSet;")
    getSourceSet = JavaMethod("()Landroid/icu/text/UnicodeSet;")
    getElements = JavaMethod("()[Landroid/icu/text/Transliterator;")
    getAvailableSources = JavaStaticMethod("()Ljava/util/Enumeration;")
    getAvailableTargets = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getAvailableVariants = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/util/Enumeration;")
    getMaximumContextLength = JavaMethod("()I")
    toRules = JavaMethod("(Z)Ljava/lang/String;")
    transliterate = JavaMultipleMethod([("(Landroid/icu/text/Replaceable;)V", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Landroid/icu/text/Replaceable;II)I", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;Ljava/lang/String;)V", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;I)V", False, False), ("(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;)V", False, False)])
    getAvailableIDs = JavaStaticMethod("()Ljava/util/Enumeration;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/icu/text/Transliterator;", True, False), ("(Ljava/lang/String;I)Landroid/icu/text/Transliterator;", True, False)])
    getID = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Ljava/lang/String;", True, False)])
    setFilter = JavaMethod("(Landroid/icu/text/UnicodeFilter;)V")
    getFilter = JavaMethod("()Landroid/icu/text/UnicodeFilter;")

    class Position(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Transliterator$Position"
        __javaconstructor__ = [("(IIII)V", False), ("(III)V", False), ("(Landroid/icu/text/Transliterator$Position;)V", False), ("()V", False)]
        contextLimit = JavaField("I")
        contextStart = JavaField("I")
        limit = JavaField("I")
        start = JavaField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        validate = JavaMethod("(I)V")
        set = JavaMethod("(Landroid/icu/text/Transliterator$Position;)V")
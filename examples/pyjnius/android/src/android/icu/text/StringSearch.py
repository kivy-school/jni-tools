from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringSearch"]

class StringSearch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/StringSearch"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/util/ULocale;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/text/RuleBasedCollator;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/text/RuleBasedCollator;Landroid/icu/text/BreakIterator;)V", False)]
    DONE = JavaStaticField("I")
    getPattern = JavaMethod("()Ljava/lang/String;")
    getCollator = JavaMethod("()Landroid/icu/text/RuleBasedCollator;")
    isCanonical = JavaMethod("()Z")
    setCanonical = JavaMethod("(Z)V")
    setCollator = JavaMethod("(Landroid/icu/text/RuleBasedCollator;)V")
    setPattern = JavaMethod("(Ljava/lang/String;)V")
    reset = JavaMethod("()V")
    setTarget = JavaMethod("(Ljava/text/CharacterIterator;)V")
    setIndex = JavaMethod("(I)V")
    getIndex = JavaMethod("()I")
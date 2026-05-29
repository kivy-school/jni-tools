from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringSearch"]

class StringSearch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/StringSearch"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/text/RuleBasedCollator;Landroid/icu/text/BreakIterator;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/text/RuleBasedCollator;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Ljava/text/CharacterIterator;Landroid/icu/util/ULocale;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getCollator = JavaMethod("()Landroid/icu/text/RuleBasedCollator;")
    setCollator = JavaMethod("(Landroid/icu/text/RuleBasedCollator;)V")
    getPattern = JavaMethod("()Ljava/lang/String;")
    setPattern = JavaMethod("(Ljava/lang/String;)V")
    isCanonical = JavaMethod("()Z")
    setCanonical = JavaMethod("(Z)V")
    setTarget = JavaMethod("(Ljava/text/CharacterIterator;)V")
    getIndex = JavaMethod("()I")
    setIndex = JavaMethod("(I)V")
    reset = JavaMethod("()V")
    handleNext = JavaMethod("(I)I")
    handlePrevious = JavaMethod("(I)I")
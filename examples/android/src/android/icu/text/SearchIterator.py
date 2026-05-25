from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchIterator"]

class SearchIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SearchIterator"
    __javaconstructor__ = [("(Ljava/text/CharacterIterator;Landroid/icu/text/BreakIterator;)V", False)]
    DONE = JavaStaticField("I")
    breakIterator = JavaField("Landroid/icu/text/BreakIterator;")
    matchLength = JavaField("I")
    targetText = JavaField("Ljava/text/CharacterIterator;")
    setIndex = JavaMethod("(I)V")
    setOverlapping = JavaMethod("(Z)V")
    setBreakIterator = JavaMethod("(Landroid/icu/text/BreakIterator;)V")
    setTarget = JavaMethod("(Ljava/text/CharacterIterator;)V")
    getMatchStart = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    getMatchLength = JavaMethod("()I")
    getBreakIterator = JavaMethod("()Landroid/icu/text/BreakIterator;")
    getTarget = JavaMethod("()Ljava/text/CharacterIterator;")
    getMatchedText = JavaMethod("()Ljava/lang/String;")
    next = JavaMethod("()I")
    previous = JavaMethod("()I")
    isOverlapping = JavaMethod("()Z")
    reset = JavaMethod("()V")
    first = JavaMethod("()I")
    following = JavaMethod("(I)I")
    last = JavaMethod("()I")
    preceding = JavaMethod("(I)I")
    setMatchLength = JavaMethod("(I)V")
    handleNext = JavaMethod("(I)I")
    handlePrevious = JavaMethod("(I)I")
    setElementComparisonType = JavaMethod("(Landroid/icu/text/SearchIterator$ElementComparisonType;)V")
    getElementComparisonType = JavaMethod("()Landroid/icu/text/SearchIterator$ElementComparisonType;")

    class ElementComparisonType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/SearchIterator/ElementComparisonType"
        values = JavaStaticMethod("()[Landroid/icu/text/SearchIterator$ElementComparisonType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/SearchIterator$ElementComparisonType;")
        STANDARD_ELEMENT_COMPARISON = JavaStaticField("Landroid/icu/text/SearchIterator/ElementComparisonType;")
        PATTERN_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator/ElementComparisonType;")
        ANY_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator/ElementComparisonType;")
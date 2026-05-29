from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchIterator"]

class SearchIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SearchIterator"
    DONE = JavaStaticField("I")
    getElementComparisonType = JavaMethod("()Landroid/icu/text/SearchIterator$ElementComparisonType;")
    getMatchedText = JavaMethod("()Ljava/lang/String;")
    isOverlapping = JavaMethod("()Z")
    preceding = JavaMethod("(I)I")
    setBreakIterator = JavaMethod("(Landroid/icu/text/BreakIterator;)V")
    setElementComparisonType = JavaMethod("(Landroid/icu/text/SearchIterator$ElementComparisonType;)V")
    setOverlapping = JavaMethod("(Z)V")
    getBreakIterator = JavaMethod("()Landroid/icu/text/BreakIterator;")
    getMatchLength = JavaMethod("()I")
    getMatchStart = JavaMethod("()I")
    following = JavaMethod("(I)I")
    reset = JavaMethod("()V")
    next = JavaMethod("()I")
    last = JavaMethod("()I")
    first = JavaMethod("()I")
    getTarget = JavaMethod("()Ljava/text/CharacterIterator;")
    setTarget = JavaMethod("(Ljava/text/CharacterIterator;)V")
    setIndex = JavaMethod("(I)V")
    getIndex = JavaMethod("()I")
    previous = JavaMethod("()I")

    class ElementComparisonType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/SearchIterator$ElementComparisonType"
        ANY_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
        PATTERN_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
        STANDARD_ELEMENT_COMPARISON = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
        values = JavaStaticMethod("()[Landroid/icu/text/SearchIterator$ElementComparisonType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/SearchIterator$ElementComparisonType;")
        ANY_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
        PATTERN_BASE_WEIGHT_IS_WILDCARD = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
        STANDARD_ELEMENT_COMPARISON = JavaStaticField("Landroid/icu/text/SearchIterator$ElementComparisonType;")
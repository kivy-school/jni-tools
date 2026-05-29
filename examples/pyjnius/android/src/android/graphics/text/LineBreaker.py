from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBreaker"]

class LineBreaker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/LineBreaker"
    BREAK_STRATEGY_BALANCED = JavaStaticField("I")
    BREAK_STRATEGY_HIGH_QUALITY = JavaStaticField("I")
    BREAK_STRATEGY_SIMPLE = JavaStaticField("I")
    HYPHENATION_FREQUENCY_FULL = JavaStaticField("I")
    HYPHENATION_FREQUENCY_NONE = JavaStaticField("I")
    HYPHENATION_FREQUENCY_NORMAL = JavaStaticField("I")
    JUSTIFICATION_MODE_INTER_CHARACTER = JavaStaticField("I")
    JUSTIFICATION_MODE_INTER_WORD = JavaStaticField("I")
    JUSTIFICATION_MODE_NONE = JavaStaticField("I")
    computeLineBreaks = JavaMethod("(Landroid/graphics/text/MeasuredText;Landroid/graphics/text/LineBreaker$ParagraphConstraints;I)Landroid/graphics/text/LineBreaker$Result;")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker$Result"
        getEndLineHyphenEdit = JavaMethod("(I)I")
        getLineBreakOffset = JavaMethod("(I)I")
        getStartLineHyphenEdit = JavaMethod("(I)I")
        hasLineTab = JavaMethod("(I)Z")
        getLineCount = JavaMethod("()I")
        getLineAscent = JavaMethod("(I)F")
        getLineDescent = JavaMethod("(I)F")
        getLineWidth = JavaMethod("(I)F")

    class ParagraphConstraints(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker$ParagraphConstraints"
        __javaconstructor__ = [("()V", False)]
        getFirstWidth = JavaMethod("()F")
        getTabStops = JavaMethod("()[F")
        getFirstWidthLineCount = JavaMethod("()I")
        setTabStops = JavaMethod("([FF)V")
        getDefaultTabStop = JavaMethod("()F")
        getWidth = JavaMethod("()F")
        setIndent = JavaMethod("(FI)V")
        setWidth = JavaMethod("(F)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker$Builder"
        __javaconstructor__ = [("()V", False)]
        setIndents = JavaMethod("([I)Landroid/graphics/text/LineBreaker$Builder;")
        build = JavaMethod("()Landroid/graphics/text/LineBreaker;")
        setBreakStrategy = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setHyphenationFrequency = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setJustificationMode = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setUseBoundsForWidth = JavaMethod("(Z)Landroid/graphics/text/LineBreaker$Builder;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker/Builder"
        __javaconstructor__ = [("()V", False)]
        setBreakStrategy = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setHyphenationFrequency = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setJustificationMode = JavaMethod("(I)Landroid/graphics/text/LineBreaker$Builder;")
        setIndents = JavaMethod("([I)Landroid/graphics/text/LineBreaker$Builder;")
        setUseBoundsForWidth = JavaMethod("(Z)Landroid/graphics/text/LineBreaker$Builder;")
        build = JavaMethod("()Landroid/graphics/text/LineBreaker;")

    class ParagraphConstraints(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker/ParagraphConstraints"
        __javaconstructor__ = [("()V", False)]
        setWidth = JavaMethod("(F)V")
        setIndent = JavaMethod("(FI)V")
        setTabStops = JavaMethod("([FF)V")
        getWidth = JavaMethod("()F")
        getFirstWidth = JavaMethod("()F")
        getFirstWidthLineCount = JavaMethod("()I")
        getTabStops = JavaMethod("()[F")
        getDefaultTabStop = JavaMethod("()F")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreaker/Result"
        getLineCount = JavaMethod("()I")
        getLineBreakOffset = JavaMethod("(I)I")
        getLineWidth = JavaMethod("(I)F")
        getLineAscent = JavaMethod("(I)F")
        getLineDescent = JavaMethod("(I)F")
        hasLineTab = JavaMethod("(I)Z")
        getStartLineHyphenEdit = JavaMethod("(I)I")
        getEndLineHyphenEdit = JavaMethod("(I)I")
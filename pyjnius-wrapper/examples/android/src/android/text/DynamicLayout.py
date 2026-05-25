from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DynamicLayout"]

class DynamicLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/DynamicLayout"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZ)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZ)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZLandroid/text/TextUtils$TruncateAt;I)V", False)]
    getLineCount = JavaMethod("()I")
    getLineTop = JavaMethod("(I)I")
    getLineDescent = JavaMethod("(I)I")
    getLineStart = JavaMethod("(I)I")
    getLineContainsTab = JavaMethod("(I)Z")
    getParagraphDirection = JavaMethod("(I)I")
    getLineDirections = JavaMethod("(I)Landroid/text/Layout$Directions;")
    getTopPadding = JavaMethod("()I")
    getBottomPadding = JavaMethod("()I")
    getEllipsizedWidth = JavaMethod("()I")
    getEllipsisStart = JavaMethod("(I)I")
    getEllipsisCount = JavaMethod("(I)I")
    getLineBreakConfig = JavaMethod("()Landroid/graphics/text/LineBreakConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/DynamicLayout/Builder"
        obtain = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/text/TextPaint;I)Landroid/text/DynamicLayout$Builder;")
        setDisplayText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/DynamicLayout$Builder;")
        setAlignment = JavaMethod("(Landroid/text/Layout$Alignment;)Landroid/text/DynamicLayout$Builder;")
        setTextDirection = JavaMethod("(Landroid/text/TextDirectionHeuristic;)Landroid/text/DynamicLayout$Builder;")
        setLineSpacing = JavaMethod("(FF)Landroid/text/DynamicLayout$Builder;")
        setIncludePad = JavaMethod("(Z)Landroid/text/DynamicLayout$Builder;")
        setUseLineSpacingFromFallbacks = JavaMethod("(Z)Landroid/text/DynamicLayout$Builder;")
        setEllipsizedWidth = JavaMethod("(I)Landroid/text/DynamicLayout$Builder;")
        setEllipsize = JavaMethod("(Landroid/text/TextUtils$TruncateAt;)Landroid/text/DynamicLayout$Builder;")
        setBreakStrategy = JavaMethod("(I)Landroid/text/DynamicLayout$Builder;")
        setHyphenationFrequency = JavaMethod("(I)Landroid/text/DynamicLayout$Builder;")
        setJustificationMode = JavaMethod("(I)Landroid/text/DynamicLayout$Builder;")
        setLineBreakConfig = JavaMethod("(Landroid/graphics/text/LineBreakConfig;)Landroid/text/DynamicLayout$Builder;")
        setUseBoundsForWidth = JavaMethod("(Z)Landroid/text/DynamicLayout$Builder;")
        setShiftDrawingOffsetForStartOverhang = JavaMethod("(Z)Landroid/text/DynamicLayout$Builder;")
        setMinimumFontMetrics = JavaMethod("(Landroid/graphics/Paint$FontMetrics;)Landroid/text/DynamicLayout$Builder;")
        build = JavaMethod("()Landroid/text/DynamicLayout;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StaticLayout"]

class StaticLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/StaticLayout"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZ)V", False), ("(Ljava/lang/CharSequence;IILandroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZ)V", False), ("(Ljava/lang/CharSequence;IILandroid/text/TextPaint;ILandroid/text/Layout$Alignment;FFZLandroid/text/TextUtils$TruncateAt;I)V", False)]
    getLineForVertical = JavaMethod("(I)I")
    getLineCount = JavaMethod("()I")
    getLineTop = JavaMethod("(I)I")
    getLineDescent = JavaMethod("(I)I")
    getLineStart = JavaMethod("(I)I")
    getParagraphDirection = JavaMethod("(I)I")
    getLineContainsTab = JavaMethod("(I)Z")
    getLineDirections = JavaMethod("(I)Landroid/text/Layout$Directions;")
    getTopPadding = JavaMethod("()I")
    getBottomPadding = JavaMethod("()I")
    getEllipsisCount = JavaMethod("(I)I")
    getEllipsisStart = JavaMethod("(I)I")
    computeDrawingBoundingBox = JavaMethod("()Landroid/graphics/RectF;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/StaticLayout/Builder"
        obtain = JavaStaticMethod("(Ljava/lang/CharSequence;IILandroid/text/TextPaint;I)Landroid/text/StaticLayout$Builder;")
        setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/StaticLayout$Builder;")
        setAlignment = JavaMethod("(Landroid/text/Layout$Alignment;)Landroid/text/StaticLayout$Builder;")
        setTextDirection = JavaMethod("(Landroid/text/TextDirectionHeuristic;)Landroid/text/StaticLayout$Builder;")
        setLineSpacing = JavaMethod("(FF)Landroid/text/StaticLayout$Builder;")
        setIncludePad = JavaMethod("(Z)Landroid/text/StaticLayout$Builder;")
        setUseLineSpacingFromFallbacks = JavaMethod("(Z)Landroid/text/StaticLayout$Builder;")
        setEllipsizedWidth = JavaMethod("(I)Landroid/text/StaticLayout$Builder;")
        setEllipsize = JavaMethod("(Landroid/text/TextUtils$TruncateAt;)Landroid/text/StaticLayout$Builder;")
        setMaxLines = JavaMethod("(I)Landroid/text/StaticLayout$Builder;")
        setBreakStrategy = JavaMethod("(I)Landroid/text/StaticLayout$Builder;")
        setHyphenationFrequency = JavaMethod("(I)Landroid/text/StaticLayout$Builder;")
        setIndents = JavaMethod("([I[I)Landroid/text/StaticLayout$Builder;")
        setJustificationMode = JavaMethod("(I)Landroid/text/StaticLayout$Builder;")
        setLineBreakConfig = JavaMethod("(Landroid/graphics/text/LineBreakConfig;)Landroid/text/StaticLayout$Builder;")
        setUseBoundsForWidth = JavaMethod("(Z)Landroid/text/StaticLayout$Builder;")
        setShiftDrawingOffsetForStartOverhang = JavaMethod("(Z)Landroid/text/StaticLayout$Builder;")
        setMinimumFontMetrics = JavaMethod("(Landroid/graphics/Paint$FontMetrics;)Landroid/text/StaticLayout$Builder;")
        build = JavaMethod("()Landroid/text/StaticLayout;")
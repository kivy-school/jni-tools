from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrecomputedText"]

class PrecomputedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/PrecomputedText"
    create = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/text/PrecomputedText$Params;)Landroid/text/PrecomputedText;")
    getParams = JavaMethod("()Landroid/text/PrecomputedText$Params;")
    getParagraphCount = JavaMethod("()I")
    getParagraphStart = JavaMethod("(I)I")
    getParagraphEnd = JavaMethod("(I)I")
    getWidth = JavaMethod("(II)F")
    getBounds = JavaMethod("(IILandroid/graphics/Rect;)V")
    getFontMetricsInt = JavaMethod("(IILandroid/graphics/Paint$FontMetricsInt;)V")
    setSpan = JavaMethod("(Ljava/lang/Object;III)V")
    removeSpan = JavaMethod("(Ljava/lang/Object;)V")
    getSpans = JavaMethod("(IILjava/lang/Class;)[Ljava/lang/Object;")
    getSpanStart = JavaMethod("(Ljava/lang/Object;)I")
    getSpanEnd = JavaMethod("(Ljava/lang/Object;)I")
    getSpanFlags = JavaMethod("(Ljava/lang/Object;)I")
    nextSpanTransition = JavaMethod("(IILjava/lang/Class;)I")
    length = JavaMethod("()I")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/PrecomputedText/Params"
        getTextPaint = JavaMethod("()Landroid/text/TextPaint;")
        getTextDirection = JavaMethod("()Landroid/text/TextDirectionHeuristic;")
        getBreakStrategy = JavaMethod("()I")
        getHyphenationFrequency = JavaMethod("()I")
        getLineBreakConfig = JavaMethod("()Landroid/graphics/text/LineBreakConfig;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/text/PrecomputedText/Params/Builder"
            __javaconstructor__ = [("(Landroid/text/TextPaint;)V", False), ("(Landroid/text/PrecomputedText$Params;)V", False)]
            setBreakStrategy = JavaMethod("(I)Landroid/text/PrecomputedText$Params$Builder;")
            setHyphenationFrequency = JavaMethod("(I)Landroid/text/PrecomputedText$Params$Builder;")
            setTextDirection = JavaMethod("(Landroid/text/TextDirectionHeuristic;)Landroid/text/PrecomputedText$Params$Builder;")
            setLineBreakConfig = JavaMethod("(Landroid/graphics/text/LineBreakConfig;)Landroid/text/PrecomputedText$Params$Builder;")
            build = JavaMethod("()Landroid/text/PrecomputedText$Params;")
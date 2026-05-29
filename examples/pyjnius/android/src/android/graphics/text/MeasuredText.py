from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeasuredText"]

class MeasuredText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/MeasuredText"
    getCharWidthAt = JavaMethod("(I)F")
    getBounds = JavaMethod("(IILandroid/graphics/Rect;)V")
    getWidth = JavaMethod("(II)F")
    getFontMetricsInt = JavaMethod("(IILandroid/graphics/Paint$FontMetricsInt;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/MeasuredText$Builder"
        __javaconstructor__ = [("(Landroid/graphics/text/MeasuredText;)V", False), ("([C)V", False)]
        HYPHENATION_MODE_FAST = JavaStaticField("I")
        HYPHENATION_MODE_NONE = JavaStaticField("I")
        HYPHENATION_MODE_NORMAL = JavaStaticField("I")
        appendReplacementRun = JavaMethod("(Landroid/graphics/Paint;IF)Landroid/graphics/text/MeasuredText$Builder;")
        setComputeHyphenation = JavaMultipleMethod([("(I)Landroid/graphics/text/MeasuredText$Builder;", False, False), ("(Z)Landroid/graphics/text/MeasuredText$Builder;", False, False)])
        setComputeLayout = JavaMethod("(Z)Landroid/graphics/text/MeasuredText$Builder;")
        appendStyleRun = JavaMultipleMethod([("(Landroid/graphics/Paint;IZ)Landroid/graphics/text/MeasuredText$Builder;", False, False), ("(Landroid/graphics/Paint;Landroid/graphics/text/LineBreakConfig;IZ)Landroid/graphics/text/MeasuredText$Builder;", False, False)])
        build = JavaMethod("()Landroid/graphics/text/MeasuredText;")
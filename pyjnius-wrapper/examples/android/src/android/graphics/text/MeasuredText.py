from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeasuredText"]

class MeasuredText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/MeasuredText"
    getWidth = JavaMethod("(II)F")
    getBounds = JavaMethod("(IILandroid/graphics/Rect;)V")
    getFontMetricsInt = JavaMethod("(IILandroid/graphics/Paint$FontMetricsInt;)V")
    getCharWidthAt = JavaMethod("(I)F")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/MeasuredText/Builder"
        __javaconstructor__ = [("([C)V", False), ("(Landroid/graphics/text/MeasuredText;)V", False)]
        HYPHENATION_MODE_FAST = JavaStaticField("I")
        HYPHENATION_MODE_NONE = JavaStaticField("I")
        HYPHENATION_MODE_NORMAL = JavaStaticField("I")
        appendStyleRun = JavaMultipleMethod([("(Landroid/graphics/Paint;IZ)Landroid/graphics/text/MeasuredText$Builder;", False, False), ("(Landroid/graphics/Paint;Landroid/graphics/text/LineBreakConfig;IZ)Landroid/graphics/text/MeasuredText$Builder;", False, False)])
        appendReplacementRun = JavaMethod("(Landroid/graphics/Paint;IF)Landroid/graphics/text/MeasuredText$Builder;")
        setComputeHyphenation = JavaMultipleMethod([("(Z)Landroid/graphics/text/MeasuredText$Builder;", False, False), ("(I)Landroid/graphics/text/MeasuredText$Builder;", False, False)])
        setComputeLayout = JavaMethod("(Z)Landroid/graphics/text/MeasuredText$Builder;")
        build = JavaMethod("()Landroid/graphics/text/MeasuredText;")
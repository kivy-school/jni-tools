from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrawableMarginSpan"]

class DrawableMarginSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/DrawableMarginSpan"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;I)V", False), ("(Landroid/graphics/drawable/Drawable;)V", False)]
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    getLeadingMargin = JavaMethod("(Z)I")
    chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getPadding = JavaMethod("()I")
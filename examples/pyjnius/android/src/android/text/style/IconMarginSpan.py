from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IconMarginSpan"]

class IconMarginSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/IconMarginSpan"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;)V", False), ("(Landroid/graphics/Bitmap;I)V", False)]
    getBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    getLeadingMargin = JavaMethod("(Z)I")
    chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getPadding = JavaMethod("()I")
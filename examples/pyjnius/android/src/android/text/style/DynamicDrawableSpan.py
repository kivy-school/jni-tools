from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DynamicDrawableSpan"]

class DynamicDrawableSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/DynamicDrawableSpan"
    __javaconstructor__ = [("()V", False)]
    ALIGN_BASELINE = JavaStaticField("I")
    ALIGN_BOTTOM = JavaStaticField("I")
    ALIGN_CENTER = JavaStaticField("I")
    getVerticalAlignment = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getSize = JavaMethod("(Landroid/graphics/Paint;Ljava/lang/CharSequence;IILandroid/graphics/Paint$FontMetricsInt;)I")
    draw = JavaMethod("(Landroid/graphics/Canvas;Ljava/lang/CharSequence;IIFIIILandroid/graphics/Paint;)V")
    getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
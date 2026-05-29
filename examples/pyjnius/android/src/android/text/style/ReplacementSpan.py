from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReplacementSpan"]

class ReplacementSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ReplacementSpan"
    __javaconstructor__ = [("()V", False)]
    getSize = JavaMethod("(Landroid/graphics/Paint;Ljava/lang/CharSequence;IILandroid/graphics/Paint$FontMetricsInt;)I")
    draw = JavaMethod("(Landroid/graphics/Canvas;Ljava/lang/CharSequence;IIFIIILandroid/graphics/Paint;)V")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    setContentDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
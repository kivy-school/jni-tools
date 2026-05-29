from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MetricAffectingSpan"]

class MetricAffectingSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/MetricAffectingSpan"
    __javaconstructor__ = [("()V", False)]
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    getUnderlying = JavaMultipleMethod([("()Landroid/text/style/MetricAffectingSpan;", False, False), ("()Landroid/text/style/CharacterStyle;", False, False)])
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnalogClock"]

class AnalogClock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AnalogClock"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setDial = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    setDialTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getDialTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setDialTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getDialTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    setHourHand = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    setHourHandTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getHourHandTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setHourHandTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getHourHandTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    setMinuteHand = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    setMinuteHandTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getMinuteHandTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setMinuteHandTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getMinuteHandTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    setSecondHand = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    setSecondHandTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getSecondHandTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setSecondHandTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getSecondHandTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    getTimeZone = JavaMethod("()Ljava/lang/String;")
    setTimeZone = JavaMethod("(Ljava/lang/String;)V")
    onVisibilityAggregated = JavaMethod("(Z)V")
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onMeasure = JavaMethod("(II)V")
    onSizeChanged = JavaMethod("(IIII)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
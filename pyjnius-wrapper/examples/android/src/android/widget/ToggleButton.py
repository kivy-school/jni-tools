from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToggleButton"]

class ToggleButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ToggleButton"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    setChecked = JavaMethod("(Z)V")
    getTextOn = JavaMethod("()Ljava/lang/CharSequence;")
    setTextOn = JavaMethod("(Ljava/lang/CharSequence;)V")
    getTextOff = JavaMethod("()Ljava/lang/CharSequence;")
    setTextOff = JavaMethod("(Ljava/lang/CharSequence;)V")
    getDisabledAlpha = JavaMethod("()F")
    onFinishInflate = JavaMethod("()V")
    setBackgroundDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    drawableStateChanged = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
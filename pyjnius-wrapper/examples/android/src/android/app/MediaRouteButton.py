from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRouteButton"]

class MediaRouteButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/MediaRouteButton"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    getRouteTypes = JavaMethod("()I")
    setRouteTypes = JavaMethod("(I)V")
    setExtendedSettingsClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    showDialog = JavaMethod("()V")
    setContentDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    performClick = JavaMethod("()Z")
    onCreateDrawableState = JavaMethod("(I)[I")
    drawableStateChanged = JavaMethod("()V")
    verifyDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)Z")
    jumpDrawablesToCurrentState = JavaMethod("()V")
    setVisibility = JavaMethod("(I)V")
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onMeasure = JavaMethod("(II)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorStateListDrawable"]

class ColorStateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ColorStateListDrawable"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/res/ColorStateList;)V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    getCurrent = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    canApplyTheme = JavaMethod("()Z")
    setAlpha = JavaMethod("(I)V")
    clearAlpha = JavaMethod("()V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getOpacity = JavaMethod("()I")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")
    onStateChange = JavaMethod("([I)Z")
    invalidateDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    scheduleDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;Ljava/lang/Runnable;J)V")
    unscheduleDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;Ljava/lang/Runnable;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getColorStateList = JavaMethod("()Landroid/content/res/ColorStateList;")
    getChangingConfigurations = JavaMethod("()I")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setColorStateList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
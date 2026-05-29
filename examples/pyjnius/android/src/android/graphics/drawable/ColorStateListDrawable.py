from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorStateListDrawable"]

class ColorStateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ColorStateListDrawable"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/res/ColorStateList;)V", False)]
    clearAlpha = JavaMethod("()V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    invalidateDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    scheduleDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;Ljava/lang/Runnable;J)V")
    unscheduleDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;Ljava/lang/Runnable;)V")
    setColorStateList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getColorStateList = JavaMethod("()Landroid/content/res/ColorStateList;")
    getChangingConfigurations = JavaMethod("()I")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getCurrent = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getOpacity = JavaMethod("()I")
    hasFocusStateSpecified = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
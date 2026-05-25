from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CheckedTextView"]

class CheckedTextView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CheckedTextView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    toggle = JavaMethod("()V")
    isChecked = JavaMethod("()Z")
    setChecked = JavaMethod("(Z)V")
    setCheckMarkDrawable = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/graphics/drawable/Drawable;)V", False, False)])
    setCheckMarkTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getCheckMarkTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setCheckMarkTintMode = JavaMethod("(Landroid/graphics/PorterDuff$Mode;)V")
    setCheckMarkTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getCheckMarkTintMode = JavaMethod("()Landroid/graphics/PorterDuff$Mode;")
    getCheckMarkTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    setVisibility = JavaMethod("(I)V")
    jumpDrawablesToCurrentState = JavaMethod("()V")
    verifyDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)Z")
    getCheckMarkDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    onRtlPropertiesChanged = JavaMethod("(I)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onCreateDrawableState = JavaMethod("(I)[I")
    drawableStateChanged = JavaMethod("()V")
    drawableHotspotChanged = JavaMethod("(FF)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
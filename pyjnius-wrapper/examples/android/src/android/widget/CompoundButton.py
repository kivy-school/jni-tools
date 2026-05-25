from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompoundButton"]

class CompoundButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CompoundButton"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    toggle = JavaMethod("()V")
    performClick = JavaMethod("()Z")
    isChecked = JavaMethod("()Z")
    setStateDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    setChecked = JavaMethod("(Z)V")
    setOnCheckedChangeListener = JavaMethod("(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V")
    setButtonDrawable = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/graphics/drawable/Drawable;)V", False, False)])
    getButtonDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setButtonIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    setButtonTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getButtonTintList = JavaMethod("()Landroid/content/res/ColorStateList;")
    setButtonTintMode = JavaMethod("(Landroid/graphics/PorterDuff$Mode;)V")
    setButtonTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getButtonTintMode = JavaMethod("()Landroid/graphics/PorterDuff$Mode;")
    getButtonTintBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    getCompoundPaddingLeft = JavaMethod("()I")
    getCompoundPaddingRight = JavaMethod("()I")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onCreateDrawableState = JavaMethod("(I)[I")
    drawableStateChanged = JavaMethod("()V")
    drawableHotspotChanged = JavaMethod("(FF)V")
    verifyDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)Z")
    jumpDrawablesToCurrentState = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    autofill = JavaMethod("(Landroid/view/autofill/AutofillValue;)V")
    getAutofillType = JavaMethod("()I")
    getAutofillValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")

    class OnCheckedChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/CompoundButton/OnCheckedChangeListener"
        onCheckedChanged = JavaMethod("(Landroid/widget/CompoundButton;Z)V")
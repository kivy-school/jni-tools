from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spinner"]

class Spinner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Spinner"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;III)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;IIILandroid/content/res/Resources$Theme;)V", False)]
    MODE_DIALOG = JavaStaticField("I")
    MODE_DROPDOWN = JavaStaticField("I")
    getPopupContext = JavaMethod("()Landroid/content/Context;")
    setPopupBackgroundDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setPopupBackgroundResource = JavaMethod("(I)V")
    getPopupBackground = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setDropDownVerticalOffset = JavaMethod("(I)V")
    getDropDownVerticalOffset = JavaMethod("()I")
    setDropDownHorizontalOffset = JavaMethod("(I)V")
    getDropDownHorizontalOffset = JavaMethod("()I")
    setDropDownWidth = JavaMethod("(I)V")
    getDropDownWidth = JavaMethod("()I")
    setEnabled = JavaMethod("(Z)V")
    setGravity = JavaMethod("(I)V")
    getGravity = JavaMethod("()I")
    setAdapter = JavaMethod("(Landroid/widget/SpinnerAdapter;)V")
    getBaseline = JavaMethod("()I")
    onDetachedFromWindow = JavaMethod("()V")
    setOnItemClickListener = JavaMethod("(Landroid/widget/AdapterView$OnItemClickListener;)V")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    performClick = JavaMethod("()Z")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    setPrompt = JavaMethod("(Ljava/lang/CharSequence;)V")
    setPromptId = JavaMethod("(I)V")
    getPrompt = JavaMethod("()Ljava/lang/CharSequence;")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    onResolvePointerIcon = JavaMethod("(Landroid/view/MotionEvent;I)Landroid/view/PointerIcon;")
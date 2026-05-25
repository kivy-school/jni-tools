from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TabWidget"]

class TabWidget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TabWidget"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onSizeChanged = JavaMethod("(IIII)V")
    getChildDrawingOrder = JavaMethod("(II)I")
    getChildTabViewAt = JavaMethod("(I)Landroid/view/View;")
    getTabCount = JavaMethod("()I")
    setDividerDrawable = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)V", False, False), ("(I)V", False, False)])
    setLeftStripDrawable = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)V", False, False), ("(I)V", False, False)])
    getLeftStripDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setRightStripDrawable = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)V", False, False), ("(I)V", False, False)])
    getRightStripDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setStripEnabled = JavaMethod("(Z)V")
    isStripEnabled = JavaMethod("()Z")
    childDrawableStateChanged = JavaMethod("(Landroid/view/View;)V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setCurrentTab = JavaMethod("(I)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    focusCurrentTab = JavaMethod("(I)V")
    setEnabled = JavaMethod("(Z)V")
    addView = JavaMethod("(Landroid/view/View;)V")
    removeAllViews = JavaMethod("()V")
    onResolvePointerIcon = JavaMethod("(Landroid/view/MotionEvent;I)Landroid/view/PointerIcon;")
    onFocusChange = JavaMethod("(Landroid/view/View;Z)V")
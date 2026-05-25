from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrameLayout"]

class FrameLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/FrameLayout"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setForegroundGravity = JavaMethod("(I)V")
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/FrameLayout$LayoutParams;")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    setMeasureAllChildren = JavaMethod("(Z)V")
    getConsiderGoneChildrenWhenMeasuring = JavaMethod("()Z")
    getMeasureAllChildren = JavaMethod("()Z")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/widget/FrameLayout$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;", False, False)])
    shouldDelayChildPressedState = JavaMethod("()Z")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/FrameLayout/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(II)V", False), ("(III)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/view/ViewGroup$MarginLayoutParams;)V", False), ("(Landroid/widget/FrameLayout$LayoutParams;)V", False)]
        UNSPECIFIED_GRAVITY = JavaStaticField("I")
        gravity = JavaField("I")
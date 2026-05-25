from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TableRow"]

class TableRow(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TableRow"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setOnHierarchyChangeListener = JavaMethod("(Landroid/view/ViewGroup$OnHierarchyChangeListener;)V")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    getVirtualChildAt = JavaMethod("(I)Landroid/view/View;")
    getVirtualChildCount = JavaMethod("()I")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/widget/TableRow$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/LinearLayout$LayoutParams;", False, False)])
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/LinearLayout$LayoutParams;")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TableRow/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(II)V", False), ("(IIF)V", False), ("()V", False), ("(I)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/view/ViewGroup$MarginLayoutParams;)V", False)]
        column = JavaField("I")
        span = JavaField("I")
        setBaseAttributes = JavaMethod("(Landroid/content/res/TypedArray;II)V")
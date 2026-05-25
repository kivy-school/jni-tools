from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TableLayout"]

class TableLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TableLayout"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setOnHierarchyChangeListener = JavaMethod("(Landroid/view/ViewGroup$OnHierarchyChangeListener;)V")
    requestLayout = JavaMethod("()V")
    isShrinkAllColumns = JavaMethod("()Z")
    setShrinkAllColumns = JavaMethod("(Z)V")
    isStretchAllColumns = JavaMethod("()Z")
    setStretchAllColumns = JavaMethod("(Z)V")
    setColumnCollapsed = JavaMethod("(IZ)V")
    isColumnCollapsed = JavaMethod("(I)Z")
    setColumnStretchable = JavaMethod("(IZ)V")
    isColumnStretchable = JavaMethod("(I)Z")
    setColumnShrinkable = JavaMethod("(IZ)V")
    isColumnShrinkable = JavaMethod("(I)Z")
    addView = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V", False, False), ("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V", False, False)])
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/widget/TableLayout$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/LinearLayout$LayoutParams;", False, False)])
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/LinearLayout$LayoutParams;")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TableLayout/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(II)V", False), ("(IIF)V", False), ("()V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/view/ViewGroup$MarginLayoutParams;)V", False)]
        setBaseAttributes = JavaMethod("(Landroid/content/res/TypedArray;II)V")
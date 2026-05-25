from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GridLayout"]

class GridLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/GridLayout"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    ALIGN_BOUNDS = JavaStaticField("I")
    ALIGN_MARGINS = JavaStaticField("I")
    BASELINE = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    BOTTOM = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    CENTER = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    END = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    FILL = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    HORIZONTAL = JavaStaticField("I")
    LEFT = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    RIGHT = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    START = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    TOP = JavaStaticField("Landroid/widget/GridLayout$Alignment;")
    UNDEFINED = JavaStaticField("I")
    VERTICAL = JavaStaticField("I")
    getOrientation = JavaMethod("()I")
    setOrientation = JavaMethod("(I)V")
    getRowCount = JavaMethod("()I")
    setRowCount = JavaMethod("(I)V")
    getColumnCount = JavaMethod("()I")
    setColumnCount = JavaMethod("(I)V")
    getUseDefaultMargins = JavaMethod("()Z")
    setUseDefaultMargins = JavaMethod("(Z)V")
    getAlignmentMode = JavaMethod("()I")
    setAlignmentMode = JavaMethod("(I)V")
    isRowOrderPreserved = JavaMethod("()Z")
    setRowOrderPreserved = JavaMethod("(Z)V")
    isColumnOrderPreserved = JavaMethod("()Z")
    setColumnOrderPreserved = JavaMethod("(Z)V")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/GridLayout$LayoutParams;")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/widget/GridLayout$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/GridLayout$LayoutParams;", False, False)])
    onViewAdded = JavaMethod("(Landroid/view/View;)V")
    onViewRemoved = JavaMethod("(Landroid/view/View;)V")
    onMeasure = JavaMethod("(II)V")
    requestLayout = JavaMethod("()V")
    onLayout = JavaMethod("(ZIIII)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    spec = JavaMultipleMethod([("(IILandroid/widget/GridLayout$Alignment;F)Landroid/widget/GridLayout$Spec;", True, False), ("(ILandroid/widget/GridLayout$Alignment;F)Landroid/widget/GridLayout$Spec;", True, False), ("(IIF)Landroid/widget/GridLayout$Spec;", True, False), ("(IF)Landroid/widget/GridLayout$Spec;", True, False), ("(IILandroid/widget/GridLayout$Alignment;)Landroid/widget/GridLayout$Spec;", True, False), ("(ILandroid/widget/GridLayout$Alignment;)Landroid/widget/GridLayout$Spec;", True, False), ("(II)Landroid/widget/GridLayout$Spec;", True, False), ("(I)Landroid/widget/GridLayout$Spec;", True, False)])

    class Alignment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/GridLayout/Alignment"

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/GridLayout/LayoutParams"
        __javaconstructor__ = [("(Landroid/widget/GridLayout$Spec;Landroid/widget/GridLayout$Spec;)V", False), ("()V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/view/ViewGroup$MarginLayoutParams;)V", False), ("(Landroid/widget/GridLayout$LayoutParams;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
        columnSpec = JavaField("Landroid/widget/GridLayout$Spec;")
        rowSpec = JavaField("Landroid/widget/GridLayout$Spec;")
        setGravity = JavaMethod("(I)V")
        setBaseAttributes = JavaMethod("(Landroid/content/res/TypedArray;II)V")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class Spec(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/GridLayout/Spec"
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsoluteLayout"]

class AbsoluteLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AbsoluteLayout"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onMeasure = JavaMethod("(II)V")
    generateDefaultLayoutParams = JavaMethod("()Landroid/view/ViewGroup$LayoutParams;")
    onLayout = JavaMethod("(ZIIII)V")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/view/ViewGroup$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;", False, False)])
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    shouldDelayChildPressedState = JavaMethod("()Z")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/AbsoluteLayout/LayoutParams"
        __javaconstructor__ = [("(IIII)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False)]
        x = JavaField("I")
        y = JavaField("I")
        debug = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
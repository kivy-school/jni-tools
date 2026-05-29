from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RadioGroup"]

class RadioGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/RadioGroup"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setOnHierarchyChangeListener = JavaMethod("(Landroid/view/ViewGroup$OnHierarchyChangeListener;)V")
    onFinishInflate = JavaMethod("()V")
    addView = JavaMethod("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V")
    check = JavaMethod("(I)V")
    getCheckedRadioButtonId = JavaMethod("()I")
    clearCheck = JavaMethod("()V")
    setOnCheckedChangeListener = JavaMethod("(Landroid/widget/RadioGroup$OnCheckedChangeListener;)V")
    generateLayoutParams = JavaMethod("(Landroid/util/AttributeSet;)Landroid/widget/RadioGroup$LayoutParams;")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/LinearLayout$LayoutParams;")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    autofill = JavaMethod("(Landroid/view/autofill/AutofillValue;)V")
    getAutofillType = JavaMethod("()I")
    getAutofillValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")
    onInitializeAccessibilityNodeInfo = JavaMethod("(Landroid/view/accessibility/AccessibilityNodeInfo;)V")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/RadioGroup/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(II)V", False), ("(IIF)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/view/ViewGroup$MarginLayoutParams;)V", False)]
        setBaseAttributes = JavaMethod("(Landroid/content/res/TypedArray;II)V")

    class OnCheckedChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/RadioGroup/OnCheckedChangeListener"
        onCheckedChanged = JavaMethod("(Landroid/widget/RadioGroup;I)V")
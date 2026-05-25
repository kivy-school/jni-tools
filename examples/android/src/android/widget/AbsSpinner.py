from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsSpinner"]

class AbsSpinner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AbsSpinner"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setAdapter = JavaMethod("(Landroid/widget/SpinnerAdapter;)V")
    onMeasure = JavaMethod("(II)V")
    generateDefaultLayoutParams = JavaMethod("()Landroid/view/ViewGroup$LayoutParams;")
    setSelection = JavaMultipleMethod([("(IZ)V", False, False), ("(I)V", False, False)])
    getSelectedView = JavaMethod("()Landroid/view/View;")
    requestLayout = JavaMethod("()V")
    getAdapter = JavaMethod("()Landroid/widget/SpinnerAdapter;")
    getCount = JavaMethod("()I")
    pointToPosition = JavaMethod("(II)I")
    dispatchRestoreInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    autofill = JavaMethod("(Landroid/view/autofill/AutofillValue;)V")
    getAutofillType = JavaMethod("()I")
    getAutofillValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimePicker"]

class TimePicker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TimePicker"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setHour = JavaMethod("(I)V")
    getHour = JavaMethod("()I")
    setMinute = JavaMethod("(I)V")
    getMinute = JavaMethod("()I")
    setCurrentHour = JavaMethod("(Ljava/lang/Integer;)V")
    getCurrentHour = JavaMethod("()Ljava/lang/Integer;")
    setCurrentMinute = JavaMethod("(Ljava/lang/Integer;)V")
    getCurrentMinute = JavaMethod("()Ljava/lang/Integer;")
    setIs24HourView = JavaMethod("(Ljava/lang/Boolean;)V")
    is24HourView = JavaMethod("()Z")
    setOnTimeChangedListener = JavaMethod("(Landroid/widget/TimePicker$OnTimeChangedListener;)V")
    setEnabled = JavaMethod("(Z)V")
    isEnabled = JavaMethod("()Z")
    getBaseline = JavaMethod("()I")
    validateInput = JavaMethod("()Z")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    dispatchProvideAutofillStructure = JavaMethod("(Landroid/view/ViewStructure;I)V")
    autofill = JavaMethod("(Landroid/view/autofill/AutofillValue;)V")
    getAutofillType = JavaMethod("()I")
    getAutofillValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")

    class OnTimeChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/TimePicker/OnTimeChangedListener"
        onTimeChanged = JavaMethod("(Landroid/widget/TimePicker;II)V")
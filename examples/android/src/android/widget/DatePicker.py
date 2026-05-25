from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatePicker"]

class DatePicker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/DatePicker"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    init = JavaMethod("(IIILandroid/widget/DatePicker$OnDateChangedListener;)V")
    setOnDateChangedListener = JavaMethod("(Landroid/widget/DatePicker$OnDateChangedListener;)V")
    updateDate = JavaMethod("(III)V")
    getYear = JavaMethod("()I")
    getMonth = JavaMethod("()I")
    getDayOfMonth = JavaMethod("()I")
    getMinDate = JavaMethod("()J")
    setMinDate = JavaMethod("(J)V")
    getMaxDate = JavaMethod("()J")
    setMaxDate = JavaMethod("(J)V")
    setEnabled = JavaMethod("(Z)V")
    isEnabled = JavaMethod("()Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    setFirstDayOfWeek = JavaMethod("(I)V")
    getFirstDayOfWeek = JavaMethod("()I")
    getCalendarViewShown = JavaMethod("()Z")
    getCalendarView = JavaMethod("()Landroid/widget/CalendarView;")
    setCalendarViewShown = JavaMethod("(Z)V")
    getSpinnersShown = JavaMethod("()Z")
    setSpinnersShown = JavaMethod("(Z)V")
    dispatchRestoreInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    dispatchProvideAutofillStructure = JavaMethod("(Landroid/view/ViewStructure;I)V")
    autofill = JavaMethod("(Landroid/view/autofill/AutofillValue;)V")
    getAutofillType = JavaMethod("()I")
    getAutofillValue = JavaMethod("()Landroid/view/autofill/AutofillValue;")

    class OnDateChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/DatePicker/OnDateChangedListener"
        onDateChanged = JavaMethod("(Landroid/widget/DatePicker;III)V")
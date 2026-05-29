from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CalendarView"]

class CalendarView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/CalendarView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setShownWeekCount = JavaMethod("(I)V")
    getShownWeekCount = JavaMethod("()I")
    setSelectedWeekBackgroundColor = JavaMethod("(I)V")
    getSelectedWeekBackgroundColor = JavaMethod("()I")
    setFocusedMonthDateColor = JavaMethod("(I)V")
    getFocusedMonthDateColor = JavaMethod("()I")
    setUnfocusedMonthDateColor = JavaMethod("(I)V")
    getUnfocusedMonthDateColor = JavaMethod("()I")
    setWeekNumberColor = JavaMethod("(I)V")
    getWeekNumberColor = JavaMethod("()I")
    setWeekSeparatorLineColor = JavaMethod("(I)V")
    getWeekSeparatorLineColor = JavaMethod("()I")
    setSelectedDateVerticalBar = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/graphics/drawable/Drawable;)V", False, False)])
    getSelectedDateVerticalBar = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setWeekDayTextAppearance = JavaMethod("(I)V")
    getWeekDayTextAppearance = JavaMethod("()I")
    setDateTextAppearance = JavaMethod("(I)V")
    getDateTextAppearance = JavaMethod("()I")
    getMinDate = JavaMethod("()J")
    setMinDate = JavaMethod("(J)V")
    getMaxDate = JavaMethod("()J")
    setMaxDate = JavaMethod("(J)V")
    setShowWeekNumber = JavaMethod("(Z)V")
    getShowWeekNumber = JavaMethod("()Z")
    getFirstDayOfWeek = JavaMethod("()I")
    setFirstDayOfWeek = JavaMethod("(I)V")
    setOnDateChangeListener = JavaMethod("(Landroid/widget/CalendarView$OnDateChangeListener;)V")
    getDate = JavaMethod("()J")
    setDate = JavaMultipleMethod([("(J)V", False, False), ("(JZZ)V", False, False)])
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class OnDateChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/CalendarView/OnDateChangeListener"
        onSelectedDayChange = JavaMethod("(Landroid/widget/CalendarView;III)V")
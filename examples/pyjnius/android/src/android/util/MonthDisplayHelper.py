from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MonthDisplayHelper"]

class MonthDisplayHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MonthDisplayHelper"
    __javaconstructor__ = [("(III)V", False), ("(II)V", False)]
    getColumnOf = JavaMethod("(I)I")
    getDayAt = JavaMethod("(II)I")
    getDigitsForRow = JavaMethod("(I)[I")
    getFirstDayOfMonth = JavaMethod("()I")
    getNumberOfDaysInMonth = JavaMethod("()I")
    getRowOf = JavaMethod("(I)I")
    getWeekStartDay = JavaMethod("()I")
    isWithinCurrentMonth = JavaMethod("(II)Z")
    nextMonth = JavaMethod("()V")
    previousMonth = JavaMethod("()V")
    getMonth = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    getYear = JavaMethod("()I")
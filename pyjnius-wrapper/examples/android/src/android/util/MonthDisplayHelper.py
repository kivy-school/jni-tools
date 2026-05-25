from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MonthDisplayHelper"]

class MonthDisplayHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MonthDisplayHelper"
    __javaconstructor__ = [("(III)V", False), ("(II)V", False)]
    getYear = JavaMethod("()I")
    getMonth = JavaMethod("()I")
    getWeekStartDay = JavaMethod("()I")
    getFirstDayOfMonth = JavaMethod("()I")
    getNumberOfDaysInMonth = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    getDigitsForRow = JavaMethod("(I)[I")
    getDayAt = JavaMethod("(II)I")
    getRowOf = JavaMethod("(I)I")
    getColumnOf = JavaMethod("(I)I")
    previousMonth = JavaMethod("()V")
    nextMonth = JavaMethod("()V")
    isWithinCurrentMonth = JavaMethod("(II)Z")
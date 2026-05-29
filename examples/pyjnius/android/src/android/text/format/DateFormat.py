from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateFormat"]

class DateFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/format/DateFormat"
    __javaconstructor__ = [("()V", False)]
    getDateFormat = JavaStaticMethod("(Landroid/content/Context;)Ljava/text/DateFormat;")
    getLongDateFormat = JavaStaticMethod("(Landroid/content/Context;)Ljava/text/DateFormat;")
    getDateFormatOrder = JavaStaticMethod("(Landroid/content/Context;)[C")
    is24HourFormat = JavaStaticMethod("(Landroid/content/Context;)Z")
    getTimeFormat = JavaStaticMethod("(Landroid/content/Context;)Ljava/text/DateFormat;")
    getBestDateTimePattern = JavaStaticMethod("(Ljava/util/Locale;Ljava/lang/String;)Ljava/lang/String;")
    getMediumDateFormat = JavaStaticMethod("(Landroid/content/Context;)Ljava/text/DateFormat;")
    format = JavaMultipleMethod([("(Ljava/lang/CharSequence;Ljava/util/Date;)Ljava/lang/CharSequence;", True, False), ("(Ljava/lang/CharSequence;J)Ljava/lang/CharSequence;", True, False), ("(Ljava/lang/CharSequence;Ljava/util/Calendar;)Ljava/lang/CharSequence;", True, False)])
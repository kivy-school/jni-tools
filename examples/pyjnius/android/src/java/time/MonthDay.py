from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MonthDay"]

class MonthDay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/MonthDay"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/MonthDay;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    of = JavaMultipleMethod([("(II)Ljava/time/MonthDay;", True, False), ("(Ljava/time/Month;I)Ljava/time/MonthDay;", True, False)])
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/MonthDay;")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    parse = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/time/MonthDay;", True, False), ("(Ljava/lang/CharSequence;Ljava/time/format/DateTimeFormatter;)Ljava/time/MonthDay;", True, False)])
    with = JavaMethod("(Ljava/time/Month;)Ljava/time/MonthDay;")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    getMonth = JavaMethod("()Ljava/time/Month;")
    now = JavaMultipleMethod([("(Ljava/time/ZoneId;)Ljava/time/MonthDay;", True, False), ("(Ljava/time/Clock;)Ljava/time/MonthDay;", True, False), ("()Ljava/time/MonthDay;", True, False)])
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    isValidYear = JavaMethod("(I)Z")
    atYear = JavaMethod("(I)Ljava/time/LocalDate;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    withDayOfMonth = JavaMethod("(I)Ljava/time/MonthDay;")
    withMonth = JavaMethod("(I)Ljava/time/MonthDay;")
    isAfter = JavaMethod("(Ljava/time/MonthDay;)Z")
    isBefore = JavaMethod("(Ljava/time/MonthDay;)Z")
    getMonthValue = JavaMethod("()I")
    getDayOfMonth = JavaMethod("()I")
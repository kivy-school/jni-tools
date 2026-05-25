from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MonthDay"]

class MonthDay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/MonthDay"
    now = JavaMultipleMethod([("()Ljava/time/MonthDay;", True, False), ("(Ljava/time/ZoneId;)Ljava/time/MonthDay;", True, False), ("(Ljava/time/Clock;)Ljava/time/MonthDay;", True, False)])
    of = JavaMultipleMethod([("(Ljava/time/Month;I)Ljava/time/MonthDay;", True, False), ("(II)Ljava/time/MonthDay;", True, False)])
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/MonthDay;")
    parse = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/time/MonthDay;", True, False), ("(Ljava/lang/CharSequence;Ljava/time/format/DateTimeFormatter;)Ljava/time/MonthDay;", True, False)])
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    getMonthValue = JavaMethod("()I")
    getMonth = JavaMethod("()Ljava/time/Month;")
    getDayOfMonth = JavaMethod("()I")
    isValidYear = JavaMethod("(I)Z")
    withMonth = JavaMethod("(I)Ljava/time/MonthDay;")
    with = JavaMethod("(Ljava/time/Month;)Ljava/time/MonthDay;")
    withDayOfMonth = JavaMethod("(I)Ljava/time/MonthDay;")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    atYear = JavaMethod("(I)Ljava/time/LocalDate;")
    compareTo = JavaMethod("(Ljava/time/MonthDay;)I")
    isAfter = JavaMethod("(Ljava/time/MonthDay;)Z")
    isBefore = JavaMethod("(Ljava/time/MonthDay;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
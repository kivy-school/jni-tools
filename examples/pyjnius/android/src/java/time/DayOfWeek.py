from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DayOfWeek"]

class DayOfWeek(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/DayOfWeek"
    MONDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    TUESDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    WEDNESDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    THURSDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    FRIDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    SATURDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    SUNDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    values = JavaStaticMethod("()[Ljava/time/DayOfWeek;")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/DayOfWeek;")
    of = JavaStaticMethod("(I)Ljava/time/DayOfWeek;")
    getValue = JavaMethod("()I")
    get = JavaMethod("(Ljava/time/temporal/TemporalField;)I")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/DayOfWeek;")
    isSupported = JavaMethod("(Ljava/time/temporal/TemporalField;)Z")
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    plus = JavaMethod("(J)Ljava/time/DayOfWeek;")
    minus = JavaMethod("(J)Ljava/time/DayOfWeek;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    MONDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    TUESDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    WEDNESDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    THURSDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    FRIDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    SATURDAY = JavaStaticField("Ljava/time/DayOfWeek;")
    SUNDAY = JavaStaticField("Ljava/time/DayOfWeek;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoPeriod"]

class ChronoPeriod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoPeriod"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    get = JavaMethod("(Ljava/time/temporal/TemporalUnit;)J")
    between = JavaStaticMethod("(Ljava/time/chrono/ChronoLocalDate;Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;")
    normalized = JavaMethod("()Ljava/time/chrono/ChronoPeriod;")
    plus = JavaMethod("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoPeriod;")
    getUnits = JavaMethod("()Ljava/util/List;")
    negated = JavaMethod("()Ljava/time/chrono/ChronoPeriod;")
    multipliedBy = JavaMethod("(I)Ljava/time/chrono/ChronoPeriod;")
    isNegative = JavaMethod("()Z")
    minus = JavaMethod("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoPeriod;")
    isZero = JavaMethod("()Z")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    subtractFrom = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
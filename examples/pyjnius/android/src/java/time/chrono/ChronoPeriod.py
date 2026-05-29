from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoPeriod"]

class ChronoPeriod(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoPeriod"
    between = JavaStaticMethod("(Ljava/time/chrono/ChronoLocalDate;Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;")
    get = JavaMethod("(Ljava/time/temporal/TemporalUnit;)J")
    getUnits = JavaMethod("()Ljava/util/List;")
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
    isZero = JavaMethod("()Z")
    isNegative = JavaMethod("()Z")
    plus = JavaMethod("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoPeriod;")
    minus = JavaMethod("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoPeriod;")
    multipliedBy = JavaMethod("(I)Ljava/time/chrono/ChronoPeriod;")
    negated = JavaMethod("()Ljava/time/chrono/ChronoPeriod;")
    normalized = JavaMethod("()Ljava/time/chrono/ChronoPeriod;")
    addTo = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    subtractFrom = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")